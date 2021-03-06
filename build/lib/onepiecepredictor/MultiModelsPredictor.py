
import abc

class MultiModelsPredictor:

    @abc.abstractmethod
    def __init__(self, X, Y, testX = None, testY = None,testTrainSplit = None,
                 folds = 5, scoring = None, performCV = None, targetEncodeCols = None):

        self.X = X
        self.Y = Y
        self.testX = testX
        self.testY = testY
        self.testTrainSplit = testTrainSplit
        self.folds = folds
        self.scoring = scoring
        self.targetEncodeCols = targetEncodeCols
        self.performCV = performCV

    @abc.abstractmethod
    def predict(self):
        pass





