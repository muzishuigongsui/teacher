from tkinter.ttk import Treeview
def tv_data(treeview,result):
    odd_row_color='#f2f2f2'
    even_row_color='#ffffff'
    treeview.tag_configure('odd',background=odd_row_color)
    treeview.tag_configure('even',background=even_row_color)
    item_num=treeview.get_children()
    if len(item_num)>0:
        for item in treeview.get_children():
            treeview.delete(item)
    for idx,item in enumerate(result):
        iid=str(idx)
        treeview.insert('','end',iid=iid,values=item,
                        tags=('even' if idx%2==0 else 'odd'))
def tv(win,lst,lst_name):
    treev=Treeview(win,columns=lst,show='headings')
    for i in range(len(lst)):
        treev.heading(lst[i],text=lst_name[i])
    return treev








