from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from LoreQ.models import *
from django.contrib import messages

# Create your views here.
def index(req):
    allmenu = MENU.objects.all()
    return render(req, "index.html", {"allmenu":allmenu}) # return Menu 

def welcome(req):
    if req.method == "POST":
        # get data
        username = req.POST["UserName"]
        Table_no = req.POST["Table_no"]
        print(username, Table_no)

        next_id = 1
        try:
            if (max([ID['id'] for ID in (USERNAME.objects.values("id"))])) >= 1:
                next_id = (max([ID['id'] for ID in (USERNAME.objects.values("id"))]))+1
        except:
            next_id = 1

        # send data to table
        uName =  USERNAME.objects.create(
            username=username,
            table_no=Table_no,
            id = next_id
        )
        uName.save() # save data into table

        # send messages and go to defind in html
        # return to main 
        return redirect(f"/inmain/{username}/{Table_no}")
    else:
        return render(req, "welcome.html")

def save_user_table(menu, price, username, Table_no, number, next_id):
    valid_menu = list(USERTABLE.objects.filter(username=username, table_no=Table_no, menu_name=menu).values("menu_name"))
    if len(valid_menu) == 0:
        create_menu = USERTABLE.objects.create(
            menu_name=menu,
            menu_price=int(price)*int(number),
            username=str(username),
            table_no=int(Table_no),
            quantity=int(number),
            id = next_id
        )
        create_menu.save()
    else:
        update_menu = USERTABLE.objects.get(menu_name=menu)
        print(update_menu.menu_price,update_menu.quantity)
        unit_price = int(update_menu.menu_price)/update_menu.quantity
        update_menu.menu_price += float(number)*(unit_price)
        update_menu.quantity += int(number)
        update_menu.save()

def index_in(req, userNAME, TableNo):
    data = USERNAME.objects.filter(username=userNAME, table_no=TableNo)
    allmenu = MENU.objects.all().values('menu_name', 'menu_price', 'description', 'menu_type')
    if req.method == "POST":
        if "AddTable" in req.POST:
            menu = req.POST["menuName"]
            price = req.POST["menuPrice"]
            username = req.POST["userName"]
            Table_no = req.POST["tableNo"]
            number = req.POST["number"]
            next_id = 1
            try:
                if (max([ID['id'] for ID in (USERTABLE.objects.values("id"))])) >= 1:
                    next_id = (max([ID['id'] for ID in (USERTABLE.objects.values("id"))]))+1
            except:
                next_id = 1
            save_user_table(menu, price, username, Table_no, number, next_id)
            return redirect(f"/inmain/{username}/{Table_no}")

    #print(allmenu)
    return render(req, "index_in.html", {"Uname":userNAME, "Tno":TableNo, "allmenu":allmenu})

def search(req, userNAME, TableNo):
    if req.method == "POST":
        menu_name = req.POST["menuName"]
        price = req.POST["menuPrice"]
        username = req.POST["userName"]
        Table_no = req.POST["tableNo"]
        number = req.POST["number"]
        next_id = 1
        try:
            if (max([ID['id'] for ID in (USERTABLE.objects.values("id"))])) >= 1:
                next_id = (max([ID['id'] for ID in (USERTABLE.objects.values("id"))]))+1
        except:
            next_id = 1
        save_user_table(menu_name, price, username, Table_no, number, next_id)
    
    search_dict = req.GET
    get_element = search_dict.get("search") # <input type="text" id="query" name="search" placeholder="Search...">
    menu = MENU.objects.filter(menu_name__contains=get_element)
    return render(req, "search.html", {"allmenu":menu, "Uname":userNAME, "Tno":TableNo})

def UserQ(req, userNAME,TableNo):
    data = USERNAME.objects.filter(username=userNAME, table_no=TableNo)
    queue_data = USERQUEUE.objects.order_by('queue_id').filter(username=userNAME, table_no=TableNo)
    queue_id = [ID["queue_id"] for ID in USERQUEUE.objects.order_by('queue_id').filter(username=userNAME, table_no=TableNo).values('queue_id')]
    print(queue_id)
    queue_detail = USERQUEUE_DETAIL.objects.order_by('queue_id').filter(queue_id__in=queue_id)
    print(queue_detail)

    return render(req, f"userQ.html", {"Uname":userNAME, "Tno":TableNo, "Qdata":queue_data, "queue_detail":queue_detail})

def UserTable(req, userNAME,TableNo):
    if req.method == "POST":
        print('****** HERE ****')
        # get data
        menuName = req.POST["menuName"] # menuName from userTable.html
        price = req.POST["price"]
        table_no = req.POST["table_no"]
        Uname = req.POST["Username"]

        # send data to table
        mTable = USERTABLE.objects.create(
            menu_name=menuName,
            menu_price=price,
            username=None,
            table_no=table_no
        )
        mTable.save()# save data into table

        return redirect("/main")
    else:
        uname = USERNAME.objects.values_list('username', flat=True).filter(username=userNAME, table_no=TableNo)
        tno = USERNAME.objects.values_list('table_no', flat=True).filter(username=userNAME, table_no=TableNo)
        prc = USERTABLE.objects.values_list('menu_price', flat=True).filter(username=userNAME, table_no=TableNo)
        number = USERTABLE.objects.values_list('quantity', flat=True).filter(username=userNAME, table_no=TableNo)
        mymenu = USERTABLE.objects.filter(username=userNAME, table_no=TableNo)

        description = PAYMENT_METHOD.objects.values_list('description')
        description = [ desc[0] for desc in description]
        return render(req, "userTable.html", 
            {"menuName":mymenu, "Uname":list(uname)[0], "Tno":list(tno)[0], "ttprice":sum(list(prc)), "number":number, "payment_method":description}) #.name , "menuPrice":mymenu.price
    
def delete_menu(req, menu_id):
    select_menu = USERTABLE.objects.get(id=menu_id)
    userNAME = list(USERTABLE.objects.filter(id=menu_id).values('username'))
    userNAME = userNAME[0]['username']
    TableNo = list(USERTABLE.objects.filter(id=menu_id).values('table_no'))
    TableNo = TableNo[0]['table_no']
    select_menu.delete()
    return redirect(f"../UserTable/{userNAME}/{TableNo}" ) #,{"menuName":mymenu, "Uname":list(uname)[0], "Tno":list(tno)[0], "ttprice":sum(list(prc)), "number":number}  .name , "menuPrice":mymenu.price

def plus_minus(req, menu_id):
    print(menu_id)
    update_quantity = USERTABLE.objects.get(id=menu_id)
    userNAME = list(USERTABLE.objects.filter(id=menu_id).values('username'))
    userNAME = userNAME[0]['username']
    TableNo = list(USERTABLE.objects.filter(id=menu_id).values('table_no'))
    TableNo = TableNo[0]['table_no']
    if 'plus' in req.POST:
        update_quantity = USERTABLE.objects.get(id=menu_id)
        update_quantity.menu_price += (update_quantity.menu_price/update_quantity.quantity)
        update_quantity.quantity += 1
        update_quantity.save()
    elif 'minus' in req.POST:
        update_quantity = USERTABLE.objects.get(id=menu_id)
        if update_quantity.quantity-1<=0:
            pass
        else:
            update_quantity.menu_price -= (update_quantity.menu_price/update_quantity.quantity)
            update_quantity.quantity -= 1
            update_quantity.save()
    return redirect(f"../UserTable/{userNAME}/{TableNo}" )

def create_queue(req, ttprice, Uname, Tno, paymentmethod):
    next_queue_id = 1
    try:
        if (max([ID['queue_id'] for ID in (USERQUEUE.objects.values("queue_id"))])) >= 1:
            next_queue_id = (max([ID['queue_id'] for ID in (USERQUEUE.objects.values("queue_id"))]))+1
    except:
        next_queue_id = 1

    mTable = USERQUEUE.objects.create(
            queue_id=next_queue_id,
            username=Uname,
            table_no=Tno,
            total_price=ttprice,
            payment_method=paymentmethod,
            status="wait"
        )
    mTable.save()# save data into table
    next_id = 1
    
    all_menu = list(USERTABLE.objects.filter(username=Uname, table_no=Tno))
    print(len(all_menu))
    for all in all_menu:
        try:
            if (max([ID['id'] for ID in (USERQUEUE_DETAIL.objects.values("id"))])) >= 1:
                next_id = (max([ID['id'] for ID in (USERQUEUE_DETAIL.objects.values("id"))]))+1
        except:
            next_id = 1
        Mname = all.menu_name
        Mprice = all.menu_price
        Quantity = all.quantity
        UQdetail_save = USERQUEUE_DETAIL.objects.create(
            id=next_id,
            queue_id=next_queue_id,
            menu_name=Mname,
            quantity=Quantity,
            price=Mprice,
        )
        UQdetail_save.save()
        
    del_menu_in_table = USERTABLE.objects.filter(username=Uname, table_no=Tno)
    del_menu_in_table.delete()
    return redirect(f"../../../../paymentsuccess/{next_queue_id}/{ttprice}/{paymentmethod}")

def paymentsuccess(req, next_queue_id, ttprice, paymentmethod):
    all_menu = list(USERQUEUE_DETAIL.objects.filter(queue_id=next_queue_id))
    date = list(USERQUEUE.objects.filter(queue_id=next_queue_id).values("date"))[0]["date"]
    time = list(USERQUEUE.objects.filter(queue_id=next_queue_id).values("time"))[0]["time"]
    return render(req, "paymentsuccess.html", {"all_menu":all_menu, "queue_no":next_queue_id, "ttprice":ttprice, "paymentmethod":paymentmethod, "date":date, "time":time})

def reportListAllQueue(req):
    Qid = list(USERQUEUE.objects.order_by('queue_id'))
    return render(req, "reportListAllQueue.html", {"Qdata":Qid})

def controlnextqueue(req):
    Qid = list(USERQUEUE.objects.order_by('queue_id').filter(status='wait'))
    return render(req, "controlnextqueue.html", {"Qdata":Qid})

def next_queue(req):
    min_queue = 1
    try:
        if (min([ID['queue_id'] for ID in (USERQUEUE.objects.filter(status="wait").values("queue_id"))]))>1:
            min_queue = min([ID['queue_id'] for ID in (USERQUEUE.objects.filter(status="wait").values("queue_id"))])
    except:
        min_queue = 1

    nextQ = USERQUEUE.objects.get(queue_id=min_queue)
    nextQ.status = "success"
    nextQ.save()

    return redirect("controlnextqueue")