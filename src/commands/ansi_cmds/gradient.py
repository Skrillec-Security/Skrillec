import os, sys, time

def gradient(startrgb, endrgb, text):
    change_r = endrgb[0] - startrgb[0] / len(text)
    change_g = endrgb[1] - startrgb[1] / len(text)
    change_b = endrgb[2] - startrgb[2] / len(text)

    r = startrgb[0]
    g = startrgb[1]
    b = startrgb[2]

    grad_text = ""
    for i in text:
        if i == '\n':
            grad_text += "\n"
        
        grad_text += "\x1b[38;2;{0};{1};{2}m{3}".format(r,g,b,i)
        r += change_r
        g += change_g
        b += change_b
    
    print(grad_text)