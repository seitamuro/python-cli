import fire

class Cli(object):
    def hello(self, num=1, name="default"):
        output = ""
        for i in range(num):
            output += "Hello, {}!\n".format(name)
        return output

if __name__ == "__main__":
    fire.Fire(Cli)
