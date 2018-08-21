import paramiko


def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    # stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction
    ssh = s.get_transport().open_session()
    print("ssh.active=======", ssh.active)
    print("stdout======", stdout.read())
    s.close()


def main():
    hostname = '47.96.251.155'
    port = 22
    username = 'Administrator'
    password = 'hmPf1grewxvHpcCpScyMOTOcDm'
    # execmd = 'cmd.exe /c PublishTool'           # windows cmd
    execmd = 'cmd.exe /c "d:/zsw/zsw"'           # windows cmd
    print("cmd:==", execmd)
    sshclient_execmd(hostname, port, username, password, execmd)
    print("ok")


if __name__ == "__main__":
    main()
