from flask import Flask, render_template

# main app
app = Flask(__name__)
 
# login
@app.route("/")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)


# # daftar
# @app.route("/")
# def daftar():
#     return render_template('daftar.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# # dasboard
# @app.route("/")
# def dasboard():
#     return render_template('dasboard.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# # our team
# @app.route("/")
# def team():
#     return render_template('team.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# # reguler

# @app.route("/")
# def Reguler():
#     return render_template('Reguler.html')

# if __name__ == "__main__":
#     app.run(debug=True)

# # VIP 
# @app.route("/")
# def VIP():
#     return render_template('VIP.html')

# if __name__ == "__main__":
#     app.run(debug=True)

# # FESTIVAL
# @app.route("/")
# def Festival():
#     return render_template('Festival.html')

# if __name__ == "__main__":
#     app.run(debug=True)


