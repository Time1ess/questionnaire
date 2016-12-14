function getOs(){
	var u=navigator.userAgent;
	if(u.indexOf('MSIE 6.0') > -1 || u.indexOf('MSIE 7.0') > -1)
	{
		alert('为了达到最佳浏览效果，我们推荐您使用Chrome浏览器或火狐浏览器');
	}
}
getOs();
