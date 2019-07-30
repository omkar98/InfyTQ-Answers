#DSA-Assgn-20
#Implement Item class here
class Item:
    def __init__(self, item_name, author_name, published_year):
        self.__item_name=item_name
        self.__author_name=author_name
        self.__published_year=published_year
    def get_item_name(self):
        return self.__item_name
    def get_author_name(self):
        return self.__author_name
    def get_published_year(self):
        return self.__published_year
    def __str__(self):
        pass
#Implement Library class here
class Library:
    def __init__(self, item_list):
        self.__item_list=item_list
    def get_item_list(self):
        return self.__item_list
    def sort_item_list_by_author(self, new_item_list):
        new_item_list.sort(key=lambda x:''.join(e for e in x.get_author_name() if e.isalnum()))
        return new_item_list
    def add_new_items(self, new_item_list):
        self.__item_list.extend(new_item_list)
        self.sort_item_list_by_author(self.__item_list)
    def sort_items_by_published_year(self):
        self.sort_item_list_by_author(self.__item_list)
        self.__item_list.sort(key=lambda x:x.get_published_year())
        
#Use different values for item and test your program
item1=Item("A Mission In Kashmir","Andrew Whitehead",1995)
item2=Item("A Passage of India","E.M.Forster",2012)
item3=Item("A new deal for Asia","Mahathir Mohammad",1999)
item4=Item("A Voice of Freedom","Nayantara Sehgal",2001)
item5=Item("A pair of blue eyes","Thomas Hardy",1998 )

item_list=[item1,item2,item3,item4,item5]
library=Library(item_list)
print("The current items in the library are:")
for item in library.get_item_list():
    print(item)

item11=Item("Broken Wing","Sarojini Naidu",2012)
item12=Item("Guide","R.K.Narayanan",2001)
item13=Item("Indian Summers","John Mathews",2001)
item14=Item("Innocent in Death","J.D.Robb",2010)
item15=Item("Life of Pi","Yann Martel",2010 )
item16=Item("Sustainability","Johny",2016)
item17=Item("Look Ahead","E.M.Freddy",2012 )

new_item_list=[item11,item12,item13,item14,item15,item16,item17]
print()
print("The new items to be added are:")
for item in new_item_list:
    print(item)

new_item_list_sorted=library.sort_item_list_by_author(new_item_list)
print()
print("The new items after sorting based on the author name are:")
for item in new_item_list_sorted:
    print(item.get_author_name())

library.add_new_items(new_item_list_sorted)
print()
print("The final set of items after adding the new item list are:")
for item in library.get_item_list():
    print(item)

library.sort_items_by_published_year()
print()
print("The items sorted based on the increasing order of their published year:")
for item in library.get_item_list():
    print(item.get_author_name() +" "+ str(item.get_published_year()))


