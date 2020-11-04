from django.shortcuts import render
import time
from django.http import JsonResponse

# Create your views here.
def bfs(request):
    context={}
    context['sleep']=time.sleep(3)
       
   
    return render(request,'bfs.html',context)

def bfs_search(request):
    context={}
    if request.method=="GET":
        node=request.GET['node']
        
        graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : [],

        }
        visited=[]
        queue=[]
        vis=[]
        visited.append(node)
        queue.append(node)
        while queue:
            s=queue.pop(0)
            vis.append(s)
    #         print(s,end=" ")
            for  neighbour  in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        if    len(visited)==1 and visited[0]=="F":
            path="You are already at final position"

        elif len(visited)==1 :
            path="Infinite path"

        else:
            path="shorestest path"
        context['path']=path
        context['visited']=vis
    # return render(request,"bfs.html",context)
    return JsonResponse(context)

