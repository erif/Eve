function getCookie(name)
{
  var offset,search,end;
  search = escape(name)+"=";
  if (document.cookie.length > 0)
  {
	offset = document.cookie.indexOf(search) 
	if (offset != (-1))
	{                                            
	  offset += search.length;
	  end = document.cookie.indexOf(";", offset);
	  if (end == (-1)) end = document.cookie.length;
	  return(unescape(document.cookie.substring(offset, end)));
	}
	else return("");
  }
  else return("");
}

function setCookie(name, value, domain)
{
	var str = escape(name)+"="+escape(value)+"; path=/;";
	if( domain ) {
		str = str+"domain="+domain+";";
	}
	document.cookie = str;
}

function deleteCookie(name)
{
  document.cookie = escape(name)+"=0; path=/; expires=Tuesday, 01-Jan-80 23:59:59 GMT";
}
