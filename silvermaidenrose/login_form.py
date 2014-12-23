
form ="""
<form method="post">
    <h1>Login</h1>
    <label>
        Username
        <input rows='1' cols='10' name="username" value=%(username_value)s></input>

    </label>
    <br>
    <label>
        Password
        <input rows='1' type='password' cols='10' name="password"></input>
    </label>
    <br>
    <font color="red">%(login_error)s</font>
    <br>
    <input type="submit" value="submit">
</form>
"""





#        <font color="red">%(password_validity_error)s</font>
#        <font color="red">%(username_error)s</font>

