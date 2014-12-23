
form ="""
<form method="post">
    <h1>Login</h1>
    <label>
        Username
        <input rows='1' cols='10' name="username" value=%(username_value)s></input>
        <font color="red">%(username_error)s</font>

    </label>
    <br>
    <label>
        Password
        <input rows='1' type='password' cols='10' name="password"></input>
        <font color="red">%(password_validity_error)s</font>
    </label>
    <br>
    <input type="submit" value="submit">
</form>
"""
