import inherit_manipul_cls_db as classes


def show_lsts():
    g.print_lst(); p.print_lst(); c.print_lst()
    print()


g = classes.GrandParent(); p = classes.Parent(); c = classes.Child()


"""show_lsts()

g.move_to_dest_cls_lst(p)

show_lsts()

p.move_to_dest_cls_lst(c)

show_lsts()

c.move_to_dest_cls_lst(g)

show_lsts()"""

show_lsts()

p.move_to_dest_cls_lst(p.child_class)

show_lsts()
