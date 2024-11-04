#world = [] # 단일 계층 구조

# world[0] : 백그라운드 객체들.. 즉 맨 아래에 그려야 할 객체들
# world[1] : 포어그라운드 객체들.. 위에 그려야할 객체들~
world = [[],[]]

def add_object(o, depth):
    world[depth].append(o)

def render():
    for layer in world:
        for o in layer:
            o.draw()
    return None


def update():
    for layer in world:
        for o in layer:
            o.update()
    return None


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 지우는 미션 달성. 다른건 지울 필요xxx
    print(' 에러 : 존재하지 않은 객체를 지운다고?')
