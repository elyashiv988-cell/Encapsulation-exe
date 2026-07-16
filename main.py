# 1 
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property 
    def name(self):
        return self.__username

profile=UserProfile("alice99")
print(profile.name)
#print(profile.__username)

# 2 

class UserProfile:
    def __init__(self, username, email):
        self.__username=username
        self.__email=email
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
profile=UserProfile("bob", "bob@mail.com")
print(profile.username)
print(profile.email)
        
# 3 

class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_username):
        if len(new_username)>=3:
            self.__username=new_username
        else:
            print("username too short")

p = UserProfile("alice")
p.username = "ab" 
p.username = "alexis"
print(p.username) 

# 4 

class UserProfile:
    def __init__(self,username):
        self.__username=username
        self.__followers=0
    @property
    def followers(self):
        return self.__followers
    def follow(self):
        self.__followers+=1
    def unfollow(self):
        self.__followers-=1 if self.__followers>0 else ""

profile=UserProfile("eli")
profile.follow()
profile.follow()
profile.follow()
profile.unfollow()
print(profile.followers)
        
# 5 

class UserProfile:
    def __init__(self,username,bio):
        self.username=username
        self.__bio=bio
    @property
    def bio(self):
        return self.__bio

class VerifiedUser(UserProfile):
    def __init__(self,username,bio,badge):
        super().__init__(username, bio)
        self.badge=badge
    def full_description(self):
        print(f"{self.username}[{self.badge}]:{self.bio}")
profile=VerifiedUser("caleb","Singer and songwriter","✓")
profile.full_description()

# 6

class UserProfile:
    def __init__(self,username,age):
        self.__username=username
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        self.__age=new_age if 13<new_age<=120 else print("Invalid age. ")
profile=UserProfile("Dan",18)
profile.age=10
profile.age=200
profile.age=25
print(profile.age)

# 7

class UserAccount:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def check_password(self,attempt):
        return True if attempt==self.__password else False
    def change_password(self,old, new):
        self.__password=new if old==self.__password else print("Incorrect old password. ")
user1=UserAccount("admin", "secret")
print(user1.check_password("worng"))
user1.change_password("secret","new123")

# 8 

class Post:
    def __init__(self,author,content):
        self.author=author
        self.content=content
        self.__likes=0
        self.__liked_by=[]
    @property
    def likes(self):
        return self.__likes
    def like(self,username):
        self.__likes+=1 if username not in self.__liked_by else +0
        self.__liked_by.append(username)
    def unlike(self,username):
        if username in self.__liked_by:
            self.__likes-=1
            self.__liked_by.remove(username)
    def status(self):
        print(f"Post by {self.author}: {self.__likes} likes.")
user2=Post("alice","Hello world!")
user2.like("dan")
user2.like("eli")
user2.like("Yishai")
user2.unlike("Yishai")
user2.status()

# 9

class UserProfile:
    def __init__(self,username):
        self.username=username
        self.__is_public=True
        self.__show_email=False
        self.__show_age=False
    @property
    def is_public(self):
        return self.__is_public
    @is_public.setter
    def is_public(self,value):
        self.__is_public=value if isinstance(value, bool) else print(f"is_public must be True or False")
    @property
    def show_email(self):
        return self.__show_email
    @show_email.setter
    def show_email(self,value):
        self.__show_email=value if isinstance(value, bool) else print(f"show_email must be True or False")
    @property
    def show_age(self):
        return self.__show_age
    @show_age.setter
    def show_age(self,value):
        self.__show_age=value  if isinstance(value, bool) else print(f"show_age must be True or False")

    def privacy_summary(self):
        print(f"is_public: {self.__is_public}|show_email:{self.__show_email}| show_age: {self.__show_age}")

profile=UserProfile("elyashiv")
profile.is_public="yes"
profile.show_email=True
profile.show_age=True
profile.privacy_summary()       
    
# 10

class UserAccount:
    def __init__(self,username,email,password,age):
        self.__username=username
        self.__email=email
        self.__password=password
        self.__age=age
        self.__logic_count=0
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_username):
        if len(new_username)>=3:
            self.__username=new_username
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self.__email=new_email
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if 13<=new_age<=120:
            self.__age=new_age
    def check_password(self,attempt):
        if attempt==self.__password:
            return self.__password
        else:
            print("worg password")
    def change_password(self,old,new):
        if self.__password==old:
            self.__password=new
        else:
            print("worg password")
        
    def login(self,password):
        if self.__password==password:
            self.__logic_count+=1
        else:
            print("Login faild. ")
    def account_summary(self):
        print(f"Username: {self.__username} | Email: {self.__email} | Login count: {self.__logic_count}")
              
user1=UserAccount("user1", "u@mail.com", "pass123", 20)
user1.login("123")
user1.login("eli")
user1.login("pass123")
user1.email="eli@988"
user1.age=24
user1.account_summary()

        

         
         
        

        
        