import numpy as np
from math import *

# Leg Measurements(mm)
l1 = 50
l2 = 100
l3 = 100

# Body Measurements(mm)
L = 234 
W = 77

def solve_legIK_L(x,y,z):
    D = (x**2+y**2-l1**2+z**2-l2**2-l3**2)/(2*l2*l3)
    theta1 = -atan2(y,x)-atan2(sqrt(x**2+y**2-l1**2),-l1)
    theta3 = atan2(sqrt(1-D**2),D)
    theta2 = atan2(z, sqrt(x**2+y**2-l1**2))-atan2(l3*sin(theta3), l2+l3*cos(theta3))
    return (theta1, theta2, theta3)

def bodyIK(omega,phi,psi,xm,ym,zm):

    Rx = np.array([
        [1, 0, 0, 0], 
        [0, np.cos(omega), -np.sin(omega), 0],
        [0,np.sin(omega),np.cos(omega),0],
        [0,0,0,1]])

    Ry = np.array([
        [np.cos(phi),0, np.sin(phi), 0], 
        [0, 1, 0, 0],
        [-np.sin(phi),0, np.cos(phi),0],
        [0,0,0,1]])

    Rz = np.array([
        [np.cos(psi),-np.sin(psi), 0,0], 
        [np.sin(psi),np.cos(psi),0,0],
        [0,0,1,0],
        [0,0,0,1]])

    Rxyz=Rx@Ry@Rz

    T = np.array([[0,0,0,xm],[0,0,0,ym],[0,0,0,zm],[0,0,0,0]])
    Tm = T+Rxyz
    
    Trb = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),-L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),-W/2],
        [0,0,0,1]])

    Trf = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),-W/2],
        [0,0,0,1]])

    Tlf = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),W/2],
        [0,0,0,1]])

    Tlb = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),-L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),W/2],
        [0,0,0,1]])
    
    return (Tlf,Trf,Tlb,Trb,Tm)

def solve(Lp,bodyIk):
    (Tlf,Trf,Tlb,Trb,Tm)=bodyIk
    
    # Invert local X
    Ix=np.array([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    
    # --- FL ---
    Q=np.linalg.inv(Tlf)@Lp[0]
    front_left = solve_legIK_L(Q[0],Q[1],Q[2])
    fl = [-front_left[0]*180/pi, front_left[1]*180/pi + 45,  front_left[2]*180/pi - 90]
    
    # --- BL ---
    Q=np.linalg.inv(Tlb)@Lp[2]
    back_left = solve_legIK_L(Q[0],Q[1],Q[2])
    bl = [-back_left[0]*180/pi, back_left[1]*180/pi + 45, back_left[2]*180/pi - 90]

    # --- FR ---
    Q=Ix@np.linalg.inv(Trf)@Lp[1]
    front_right = solve_legIK_L(Q[0],Q[1],Q[2])
    fr = [-front_right[0]*180/pi, front_right[1]*180/pi + 45, front_right[2]*180/pi - 90]

    # --- BR ---
    Q=Ix@np.linalg.inv(Trb)@Lp[3]
    back_right = solve_legIK_L(Q[0],Q[1],Q[2])
    br = [-back_right[0]*180/pi, back_right[1]*180/pi + 45, back_right[2]*180/pi - 90]
    
    return np.array ([fl, bl, br, fr])
