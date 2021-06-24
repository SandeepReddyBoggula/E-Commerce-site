from django.shortcuts import render, redirect  
from product.forms import DeletedForm, ProductForm  
from product.models import Deleted, Product 

# Create your views here.

#This code is for main manu 
def main(request):
    return  render(request,'basic.html') 
 
#This is insertion code  

def pro(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form}) 

#This Code is to retrive the information from database

def show(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products})  

#This code is to update the information

def edit(request, id):
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})   
    

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})  


        
#This Code is for deleting a record temparorily .

def edit_delete(request,id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit_delete.html', {'product':product})  

def delete_save(request, id):  
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = DeletedForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                product.delete()
                return redirect("/show")
            except:
                pass
    else:
        form=  DeletedForm()  
    return render(request, 'edit_delete.html', {'product': product})

def deleted(request):  
    deletes = Deleted.objects.all()  
    return render(request,"deleted.html",{'deletes':deletes})

#This Code is for deleting the infomation permanantly

def destroy(request, id):  
    product = Deleted.objects.get(id=id)
    product.delete()  
    return redirect("/deleted") 

#This Code is to Restore information


def edit_restore(request,id):  
    product = Deleted.objects.get(id=id)  
    return render(request,'restore_edit.html', {'product':product})  

def restore_save(request, id):  
    product = Deleted.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                product.delete()
                return redirect("/show")
            except:
                pass
    else:
        form=  ProductForm()  
    return render(request, 'restore_edit.html', {'product': product})