from django.shortcuts import render
from neuralnetwork.forms import MatrixForm
from neuralnetwork.newnural import testtest
import ast

def index(request):
    
    if request.method == 'POST':
        form = MatrixForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            matrix = cd['matrix']
            print(matrix)
            matrixList = ast.literal_eval(matrix)
            res1 = testtest(matrixList)
        return render(request, 'neuralnetwork/res.html', {'res1':res1})
    else:
        form = MatrixForm()
        context = {'form':form}
    return render(request, 'neuralnetwork/index.html', context)
