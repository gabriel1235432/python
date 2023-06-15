import time

def coutdown_timer(seconds):
    
    while seconds > 0:

        mins = (seconds / 60)
        secs = (seconds % 60)

        timer = f'{mins}:{secs}'
        time.sleep(1)
        print(timer)

        seconds -= 1
    print('Tempo Esgotado!')

seconds = input("digite o tempo em segundos:  ")      
coutdown_timer(int(seconds))