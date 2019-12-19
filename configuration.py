class Configuration:
    def __init__(self,t):
        self.t = tuple(t)
    def moves(self):
        z= self.t.index(0)
        r= len(self.t)
        my_moves= set()
        for i in range(r):
            l= list(self.t)
            up_to_2 = len(l[i:z])
            after_2 = len(l[z:i])
            if (up_to_2 <= 2 and up_to_2 > 0) or  (after_2 <= 2 and after_2 > 0):
                l[i],l[z] = l[z], l[i]
                my_moves.add(Configuration(tuple(l)))
        return my_moves


    def __eq__(self,other):
        if isinstance(other, Configuration):
            return self.t == other.t
        return False
    def __hash__(self):
        return hash(self.t)

    def add(self, i):
        l= list(self.t)
        l.append(i)
        self.t=tuple(l)

    @classmethod
    def configs(cls,pennies, dimes, spaces=1):
        config_set= set()
        if pennies < 0 or dimes < 0 or spaces < 0:
            return config_set
        if pennies+dimes+spaces == 1:
            if pennies==1:
                c= Configuration([1])
                config_set.add(c)
            if dimes ==1:
                c= Configuration([10])
                config_set.add(c)
            if spaces ==1:
                c= Configuration([0])
                config_set.add(c)
            return config_set
        s1= cls.configs(pennies-1,dimes,spaces)
        s2= cls.configs(pennies, dimes-1, spaces)
        s3= cls.configs(pennies, dimes, spaces-1)
        for i in s1:
            i.add(1)
            config_set.add(i)
        for i in s2:
            i.add(10)
            config_set.add(i)
        for i in s3:
            i.add(0)
            config_set.add(i)
        return config_set

# confs = Configuration.configs(2,1)
# print([i.t for i in confs])
