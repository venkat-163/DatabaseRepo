from flask import Flask,jsonify,request
import json
from Components import LoginAndSignup,EmployeeTicketOperation,AdminteamOperation,AdminOperation
import psycopg2

#data base connection :

connection = psycopg2.connect(
        host="localhost",
        database="TicketSystem",
        user="postgres",
        password="digit@A0")


app = Flask(__name__)

#**************these are login releted APIS ******************************
@app.route('/signup',methods = ['POST'])
def signUpService():
    employeeSignUPData = request.json
    return LoginAndSignup.employeeSignUP(connection,employeeSignUPData)

@app.route('/login',methods = ['GET'])
def loginService():
    employeeLogInData = request.json
    return LoginAndSignup.employeeLogIN(connection,employeeLogInData)

@app.route('/adminlogin',methods = ['GET'])
def adminloginService():
    adminLoginData = request.json
    return LoginAndSignup.adminLogin(connection,adminLoginData)

@app.route('/adminteamlogin',methods = ['GET'])
def adminTeamloginService():
    teamlogInData = request.json
    return LoginAndSignup.teamlogin(connection,teamlogInData)

#******************************************************************************

#**************these emmployee operation API******************************

@app.route('/create',methods = ['POST'])
def createTicket():
    ticketData = request.json
    return EmployeeTicketOperation.createTicket(connection,ticketData)

@app.route('/employeeticket',methods = ['GET'])
def getEmployeeTickets():
    employeeData = request.json
    return EmployeeTicketOperation.getEmployeeTickets(connection,employeeData)


@app.route('/editTicket',methods = ['POST'])
def editEmployeeTicket():
    ticketData = request.json
    return EmployeeTicketOperation.editEmployeeTicket(connection,ticketData)

@app.route('/delete',methods = ['DELETE'])
def deleteTicket():
    deleteData = request.json
    return EmployeeTicketOperation.deleteTicket(connection,deleteData)

#*****************************************************************************

##************admin team operations ************************************8

@app.route('/adminteamticket',methods = ['GET'])
def getAdminteamticket():
    adminteamData = request.json
    return AdminteamOperation.getAdminteamticket(connection,adminteamData)


@app.route('/changestatus',methods = ['POST'])
def changeStatus():
    statusData = request.json
    return AdminteamOperation.changeStatus(connection,statusData)

#*****************************************************************************

#*************************admin operations*******************

@app.route('/getAllTickets',methods = ['GET'])
def getAdminTickets():
    return AdminOperation.getAdminTickets(connection)

@app.route('/getAdminteam',methods = ['GET'])
def getAdminTeamMembers():
    return AdminOperation.getAdminTeamMembers(connection)

@app.route('/assignTicket',methods = ['POST'])
def assignEmployeeTicket():
    assignData = request.json
    return AdminOperation.assignEmployeeTicket(connection,assignData)



app.run()