# dasboard
@app.route("/")
def dasboard():
    return render_template('dasboard.html')

if __name__ == "__main__":
    app.run(debug=True)