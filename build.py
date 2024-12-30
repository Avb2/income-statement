from tkinter import *


class CreateHome:
    def __init__(self):
        self.root = Tk()
        self.title = self.root.title('Income Statement')
        self.incomeLabels = ['Sales', 'Cogs', 'Gross Profit', 'Operating Expense', 'Depreciation', 'Operating Profit',
                             'Taxes', 'Interest', 'EBIT', 'Net Income']
        self.grossProfit = 0
        self.opProfit = 0
        self.EBIT = 0
        self.netIncome = 0

    def buildPage(self):
        labelsFrame = Frame(self.root)
        labelsFrame.grid(row=0, column=0)
        buttonFrame = Frame(self.root)
        buttonFrame.grid(row=1, column=0)
        incomeStmtLabels = self.createLabels(labelsFrame)
        self.createEnterButton(
            sales=incomeStmtLabels[0],
            cogs=incomeStmtLabels[1],
            grossProfitLabel=incomeStmtLabels[2],
            operatingExpense=incomeStmtLabels[3],
            depreciation=incomeStmtLabels[4],
            opProfitLabel=incomeStmtLabels[5],
            taxes=incomeStmtLabels[6],
            interest=incomeStmtLabels[7],
            EBITlabel=incomeStmtLabels[8],
            netIncomeLabel= incomeStmtLabels[9],
            buttonFrame=buttonFrame
        )
        self.createClearButton(buttonFrame)
        self.root.mainloop()

    def createLabels(self, labelsFrame):
        incomeStmtLabels = []

        for index, label in enumerate(self.incomeLabels):
            categoryLabel = Label(labelsFrame, text=label, borderwidth=2, relief='groove', width=20, height=1)
            categoryLabel.grid(row=index, column=0)
            if index == 2:
                label = Label(labelsFrame, text=self.grossProfit)
                label.grid(row=index, column=1)
                incomeStmtLabels.append(label)
            elif index == 5:
                label = Label(labelsFrame, text=self.opProfit)
                label.grid(row=index, column=1)
                incomeStmtLabels.append(label)
            elif index == 8:
                label = Label(labelsFrame, text=self.EBIT)
                label.grid(row=index, column=1)
                incomeStmtLabels.append(label)
            elif index == 9:
                label = Label(labelsFrame, text=self.netIncome)
                label.grid(row=index, column=1)
                incomeStmtLabels.append(label)
            else:
                label = Entry(labelsFrame, borderwidth=2, relief='groove', width=20)
                label.grid(row=index, column=1)
                incomeStmtLabels.append(label)

        self.root.update_idletasks()
        print(incomeStmtLabels)
        return incomeStmtLabels

    def createEnterButton(self, sales, cogs, grossProfitLabel, operatingExpense, depreciation,
                          opProfitLabel, taxes, interest, EBITlabel, netIncomeLabel, buttonFrame):

        enter = Button(buttonFrame, text='Enter', width=10, command=lambda: self.calculateInputFields(
            sales=sales,
            cogs=cogs,
            grossProfitLabel=grossProfitLabel,
            operatingExpense=operatingExpense,
            depreciation=depreciation,
            opProfitLabel=opProfitLabel,
            taxes=taxes,
            interest=interest,
            EBITlabel=EBITlabel,
            netIncomeLabel=netIncomeLabel,
        ))
        enter.grid(row=0, column=1)

    def calculateInputFields(self, sales, cogs, grossProfitLabel, operatingExpense, depreciation, opProfitLabel,
                             taxes, interest, EBITlabel, netIncomeLabel):
        self.calculateGrossProfit(sales, cogs, grossProfitLabel)
        self.calculateOpProfit(operatingExpense, depreciation, opProfitLabel)
        self.calculateEBIT(taxes, interest, EBITlabel)
        self.setNetIncome(netIncomeLabel)

    def calculateGrossProfit(self, sales, cogs, grossProfitLabel):
        self.grossProfit = float(sales.get()) - float(cogs.get())
        grossProfitLabel.config(text=self.grossProfit)


    def calculateOpProfit(self, operatingExpense, depreciation, opProfitLabel):
        self.opProfit = self.grossProfit - float(operatingExpense.get()) - float(depreciation.get())
        opProfitLabel.config(text=self.opProfit)

    def calculateEBIT(self, taxes, interest, EBITlabel):
        self.EBIT = self.opProfit - float(taxes.get()) - float(interest.get())
        EBITlabel.config(text=self.EBIT)

    def setNetIncome(self, netIncomeLabel):
        self.netIncome = self.EBIT
        netIncomeLabel.config(text=self.netIncome)

    def clearIncomeStmt(self):
        self.EBIT, self.netIncome, self.grossProfit, self.opProfit = 0, 0, 0, 0

    def createClearButton(self, buttonFrame):
        clearButton = Button(buttonFrame, text='Clear', width=10, command=lambda: self.clearIncomeStmt())
        clearButton.grid(row=0, column=0)