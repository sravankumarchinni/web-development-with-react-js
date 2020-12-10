# -*- coding: utf-8 -*-
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days=10):
        #pass
        b = BookItem(self,name)
        self.BookItem.remove(b)
        self.total_count -=1
    
    #assume name is unique
    def returnBook(self,name):
        #pass
        b = BookItem(self,name)
        self.BookItem.append(b)
        self.total_count +=1
        
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        #pass
        b = BookItem(self,name,author,publish_date,pages)
        self.name=name
        self.author=author
        self.publish_date=publish_date
        self.pages=pages
        self.book_item.append(b)
        self.total_count +=1
        
    
    def removeBook(self,name):
        #pass
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -=1
    
    def removeBookItemFromCatalog(self,catalog,book,isbn):
        #pass
        if book in self.catalog:
            self.catalog.remove(book)
            self.total_count -=1
        
    
