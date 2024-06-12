// 在 script.js 中添加以下代码

const dynamicContent = document.querySelector('.dynamic-content');

function scrollContent() {
    dynamicContent.scrollLeft += dynamicContent.offsetWidth;
}
dynamicContent.addEventListener('scroll', function() {
    // 如果滚动到了最后一个动态内容项，返回到第一个
    if (dynamicContent.scrollLeft + dynamicContent.clientWidth >= dynamicContent.scrollWidth) {
        dynamicContent.scrollLeft = 0;
    }
});

// 每隔固定时间，滚动到下一个动态内容项
setInterval(scrollContent, 3000); // 3秒钟滚动一次
