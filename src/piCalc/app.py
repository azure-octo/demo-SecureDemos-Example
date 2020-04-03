import time

import requests
import os
from decimal import Decimal as Dec, getcontext as gc

# dapr Config --------------------------------------------------------------------------------------------

dapr_port = os.getenv("DAPR_HTTP_PORT", default="3500")

## dapr Functions ----------------------------------------------------------------------------------------

def getState(maxK, prec, disp):
    req = requests.get(f"http://localhost:{dapr_port}/v1.0/state/piState")
    try:
        state = req.json()
        if (int(state['maxK'])==maxK and int(state['prec'])==prec and int(state['disp'])==disp):
            return state
    except ValueError:
        print("ERROR")
        pass

    return None

def saveState(K,M,L,X,S,k,maxK,prec,disp):
    try:
        content = [{
            "key":"piState",
            "value":{
                "M": str(M),
                "L": str(L),
                "X": str(X),
                "S": str(S),
                "K": str(K),
                "k": str(k),
                "maxK": str(maxK),
                "prec": str(prec),
                "disp": str(disp)
            }}]
        header={"Content-Type":"application/json"}

        requests.post(f"http://127.0.0.1:{dapr_port}/v1.0/state", json=content, headers=header)
    except Exception as e:
        print(e, flush=True)
        return False

    return True

def storePi(maxK,prec,disp,pi):
    try:
        content = {
            "data":{
                "id":str(maxK),
                "maxK":str(maxK),
                "prec":str(prec),
                "disp":str(disp),
                "Pi":str(pi)
                }
            }
        header  = {"Content-Type":"application/json"}

        requests.post(f"http://localhost:{dapr_port}/v1.0/bindings/piStore", json=content, headers=header)
    except Exception as e:
        print(e, flush=True)
        return False

    return True

# Pi Function -------------------------------------------------------------------------------------------------

## Calulate Pi w/ Chudnovsky Algorithm
# https://en.wikipedia.org/wiki/Chudnovsky_algorithm
def PI(maxK=70, prec=1008, disp=1007, K=6, M=1, L=13591409, X=1, S=13591409, ki=1):
    gc().prec = prec

    '''
    state = getState(maxK, prec, disp)
    if state != None:
        K,M,L,X,S,ki = int(state['K']),int(state['M']),int(state['L']),int(state['X']),Dec(state['S']),int(state['k'])
    '''

    for k in range(ki, maxK+1):
        M = (K**3 - 16*K) * M // k**3 
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
        #saveState(K,M,L,X,S,k,maxK,prec,disp) 
        print(f'k:{k}', flush=True)
    
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp])
    print("PI(maxK={} iterations, gc().prec={}, disp={} digits) =\n{}".format(maxK, prec, disp, pi))
    return pi

# Main --------------------------------------------------------------------------------------------------------------

maxK, prec, disp = 500, 10000, 10000
Pi = PI(maxK,prec,disp)

#storePi(maxK, prec, disp, Pi)
