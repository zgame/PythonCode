---------------------------------------------------------------------------------------------------------------------
-- 生成机器人,@Num:指定生成数量，一半名字使用游客***，一半的名字读取AndroidUserName，

DECLARE @Accounts NVARCHAR(32)
DECLARE @Num INT
DECLARE @FaceId INT
DECLARE @ServerID INT
DECLARE @VipLevel INT
DECLARE @FaceUrl NVARCHAR(256)
DECLARE @FaceHttp NVARCHAR(256)
DECLARE @NameCount INT
DECLARE @AndroidCount INT
DECLARE @NickName NVARCHAR(64)

SET @Num = {num}
SET @FaceId = 1
SET @VipLevel = 0

-- 以下数据需要修改
-- 设置服务器ID
SET @ServerID = {serverID}
-- 设置头像的地址
SET @FaceHttp='http://dl.yx.soonyo.com/tb/robot/'

--读取机器人名字
SELECT id=identity(int,1,1), Name INTO #regtemp11 FROM AndroidUserName(NOLOCK)
--取名字数量
SELECT @NameCount=COUNT(*) FROM #regtemp11
--取机器人数量
SELECT @AndroidCount=COUNT(*) FROM AccountsInfo(NOLOCK) WHERE IsAndroid=1

-- WHILE @Num < 100
BEGIN
	-- 生成账号
	SET @Accounts = N'JQL_CHECK_D' + cast((@ServerID*100+@Num) AS NVARCHAR(32))
	SET @AndroidCount=@AndroidCount+1
-- 	SET @Num = @Num + 1
	SET @VipLevel=RAND()*7+1
	-- 设置头像
	SET @FaceId = cast( floor(RAND()*6) AS INT) + 1
	SET @FaceUrl=@FaceHttp+CAST(CAST(RAND()*200+1 AS INT) AS NVARCHAR)+'.jpg'
	SELECT @NickName=Name FROM #regtemp11 WHERE id=(@AndroidCount-1)%@NameCount+1
	-- 注册用户
	INSERT dbo.AccountsInfo (Accounts,NickName,RegAccounts,LogonPass,InsurePass,IsAndroid,RegisterIP,LastLogonIP,VipLev,FaceID,FaceUrl)
	VALUES (@Accounts,@NickName,@Accounts,'96E79218965EB72C92A549DD5A330112','96E79218965EB72C92A549DD5A330112',1,'127.0.0.1','127.0.0.1',@VipLevel,@FaceId,@FaceUrl)

	-- GameID
	DECLARE @UserID INT
	UPDATE dbo.AccountsInfo SET @UserID=UserID, GameID=dbo.GSP_FUN_GetGameID(@UserID, RAND(), RAND()) WHERE Accounts=@Accounts

	-- 将机器人插入记录表
	INSERT INTO dbo.AndroidManager(UserID, ServerID, ServiceGender, MinPlayDraw, MaxPlayDraw, MinTakeScore, MaxTakeScore, MinReposeTime, MaxReposeTime, ServiceTime) 
	VALUES(@UserID, @ServerID, 7, 1, 100, 800000, 500000000,30,360,16777215 )
END

 
DROP TABLE #regtemp11

---------------------------------------------------------------------------------------------------------------------


