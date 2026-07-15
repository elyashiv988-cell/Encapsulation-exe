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
profile=VerifiedUser("caleb","Singer and songwriter","v")
profile.full_description()
   
         
        

        
        