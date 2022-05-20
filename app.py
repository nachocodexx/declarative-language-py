import yaml


class JulitoNode(object):

    def __init__(self,name,port,environments):
        self.name         = name
        self.port         = port
        self.environments = environments


class ComposeFile(object):
    def __init__(self,version,services):
        self.version  = version
        self.services = services



if __name__ == "__main__":
    d  = JulitoNode("jp",8000,{"MEMORY":2000})
    cf = ComposeFile("3.7",  {"jp":d} )
    x  = yaml.dump(cf.__dict__)
    with open("t.yml","w") as f:
        f.write(x)
    print(x)
