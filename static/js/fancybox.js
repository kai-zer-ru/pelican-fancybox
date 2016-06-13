function activate_fancybox() {
	imgs = $(".article-content").find("img");
	$(imgs).each(function(i,img) {
		$(img).parent().wrapInner("<a class='fancybox' rel='galery' href='" + $(img).attr("src") + "'>", "</a>");
	});
}