from abc import ABC,abstractmethod


class Model(ABC):
    @abstractmethod
    def train(self,data):
        pass
    @abstractmethod
    def predict(self,input):
        pass

class AverageModel(Model):
    def train(self,data):
        return sum(data) / len(data)
    def predict(self,input):
        pass

class ModeleLineaireSimple(Model):
    def __init__(self,width,bias):
        self.width = width
        self.bias = bias
    def train(self,data):
        pass
    def predict(self,input):
        return self.width * input + self.bias

class Pipeline:
    def __init__(self,pretreatment,modele):
        self.pretreatment = pretreatment
        self.modele = modele
    def execute(self,data, input):
        result = self.modele.train(self.pretreatment(data)) or self.modele.predict(input)
        return result


def normalize(data):
    maximum = max(data)
    return [d/maximum for d in data]

#TypeError
# model = Model()

# data = [5, 8, 11]
# modele = AverageModel()
# print(modele.train(data))
# modele.predict(999)

# modele = ModeleLineaireSimple(width=2, bias=1)
# modele.train(None)
# print(modele.predict(5))

pipeline_mean = Pipeline(normalize,AverageModel())
pipeline_lineaire = Pipeline(normalize,ModeleLineaireSimple(2,1))
data = [5,8,11]
for pipeline in [pipeline_mean,pipeline_lineaire]:
    result = pipeline.execute(data,input=5)
    print(type(pipeline.modele).__name__," => ",result)