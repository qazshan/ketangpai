
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#165DFF',
                secondary: '#0FC6C2',
                neutral: '#F5F7FA',
                dark: '#1D2129',
            },
            fontFamily: {
                inter: ['Inter', 'system-ui', 'sans-serif'],
            },
        }
    }
}
< / script >
< style
type = "text/tailwindcss" >


@layer


utilities
{
.content - auto
{
    content - visibility: auto;
}
.nav - link - hover
{
@ apply
relative
overflow - hidden
transition - all
duration - 300;
}
.nav - link - hover::after
{
    content: '';
@ apply
absolute
bottom - 0
left - 0
w - 0
h - 0.5
bg - primary
transition - all
duration - 300;
}
.nav - link - hover: hover::after
{
@ apply
w - full;
}
.tab - content
{
@ apply
hidden
opacity - 0
transition - all
duration - 500
ease - in -out;
}
.tab - content.active
{
@ apply
block
opacity - 100;
}
}
< / style >
< / head >
< body


class ="font-inter bg-gray-50 text-dark" >

< div


class ="container mx-auto px-4 py-6" >

< !-- 头部区域 -->
< header


class ="mb-8" >

< div


class ="flex flex-col md:flex-row justify-between items-center mb-4" >

< div


class ="flex items-center mb-4 md:mb-0" >

< div


class ="bg-primary text-white p-3 rounded-lg mr-3" >

< i


class ="fa-solid fa-graduation-cap text-2xl" > < / i >

< / div >
< div >
< h1


class ="text-2xl font-bold text-dark" > 课程学习平台 < / h1 >

< p


class ="text-gray-500 text-sm" > 提升你的专业技能 < / p >

< / div >
< / div >
< div


class ="flex items-center space-x-4" >

< div


class ="relative" >

< input
type = "text"
placeholder = "搜索课程..."


class ="pl-10 pr-4 py-2 rounded-full border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all" >

< i


class ="fa-solid fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" > < / i >

< / div >
< div


class ="flex items-center space-x-3" >

< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-regular fa-bell text-xl" > < / i >

< / button >
< div


class ="h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center text-primary" >

< span


class ="font-medium" > 张 < / span >

< / div >
< / div >
< / div >
< / div >

< !-- 课程信息卡片 -->
< div


class ="bg-white rounded-xl shadow-sm p-6 mb-6 border border-gray-100" >

< div


class ="flex flex-col md:flex-row items-start md:items-center" >

< img
src = "https://picsum.photos/seed/course/200/100"
alt = "Python编程基础"


class ="rounded-lg mb-4 md:mb-0 md:mr-6 w-full md:w-48 h-24 md:h-auto object-cover" >

< div


class ="flex-1" >

< div


class ="flex items-center mb-2" >

< span


class ="bg-primary/10 text-primary text-xs font-medium px-2.5 py-0.5 rounded-full mr-2" > 基础课程 < / span >

< span


class ="bg-green-100 text-green-600 text-xs font-medium px-2.5 py-0.5 rounded-full" > 进行中 < / span >

< / div >
< h2


class ="text-xl font-bold mb-2" > Python编程基础 < / h2 >

< p


class ="text-gray-600 text-sm mb-4" > 掌握Python编程语言的基础语法和常用编程技巧，为后续的数据分析和人工智能学习打下坚实基础。 < / p >

< div


class ="flex flex-wrap items-center gap-4 text-sm" >

< div


class ="flex items-center text-gray-500" >

< i


class ="fa-regular fa-calendar mr-1" > < / i >

< span > 16
周课程 < / span >
< / div >
< div


class ="flex items-center text-gray-500" >

< i


class ="fa-regular fa-clock mr-1" > < / i >

< span > 共48课时 < / span >
< / div >
< div


class ="flex items-center text-gray-500" >

< i


class ="fa-solid fa-user mr-1" > < / i >

< span > 李教授 < / span >
< / div >
< div


class ="flex items-center text-gray-500" >

< i


class ="fa-regular fa-user mr-1" > < / i >

< span > 2, 345
人已学习 < / span >
< / div >
< / div >
< / div >
< div


class ="mt-4 md:mt-0" >

< button


class ="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded-lg transition-all flex items-center" >

< i


class ="fa-solid fa-play-circle mr-2" > < / i >


继续学习
< / button >
< / div >
< / div >
< / div >
< / header >

< !-- 主内容区域 -->
< main


class ="bg-white rounded-xl shadow-sm p-6 border border-gray-100" >

< !-- 导航栏 -->
< div


class ="mb-6" >

< nav


class ="flex flex-wrap border-b border-gray-200" >

< ul


class ="flex flex-wrap -mb-px text-sm font-medium text-center" >

< li


class ="mr-2" >

< button


class ="tab-button active inline-block p-4 border-b-2 border-primary text-primary rounded-t-lg nav-link-hover" data-tab="catalog" >

< i


class ="fa-solid fa-list-ul mr-2" > < / i > 目录

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="课件" >

< i


class ="fa-solid fa-desktop mr-2" > < / i > 互动课件

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="作业" >

< i


class ="fa-solid fa-file-lines mr-2" > < / i > 作业

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="测试" >

< i


class ="fa-solid fa-question-circle mr-2" > < / i > 测试

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="会议" >

< i


class ="fa-solid fa-video mr-2" > < / i > 腾讯会议

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="公告" >

< i


class ="fa-solid fa-bullhorn mr-2" > < / i > 公告

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="话题" >

< i


class ="fa-solid fa-comments mr-2" > < / i > 话题

< / button >
< / li >
< li


class ="mr-2" >

< button


class ="tab-button inline-block p-4 border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 rounded-t-lg nav-link-hover" data-tab="答题" >

< i


class ="fa-solid fa-poll mr-2" > < / i > 互动答题

< / button >
< / li >
< / ul >
< / nav >
< / div >

< !-- 内容区域 -->
< div


class ="tab-content-container" >

< !-- 目录内容 -->
< div
id = "catalog"


class ="tab-content active" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 课程目录 < / h3 >

< div


class ="flex space-x-2" >

< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-chevron-up" > < / i >

< / button >
< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-chevron-down" > < / i >

< / button >
< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-expand" > < / i >

< / button >
< / div >
< / div >

< div


class ="space-y-2" >

< !-- 章节1 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden" >

< div


class ="bg-neutral px-4 py-3 flex justify-between items-center cursor-pointer" >

< div


class ="flex items-center" >

< i


class ="fa-solid fa-chevron-down text-gray-500 mr-3 transition-transform" > < / i >

< h4


class ="font-medium" > 第1章 Python基础 < / h4 >

< / div >
< div


class ="text-xs text-gray-500" > 4课时 < / div >

< / div >
< div


class ="p-4 space-y-3 bg-white" >

< div


class ="flex items-center p-2 hover:bg-gray-50 rounded-lg transition-colors" >

< div


class ="flex-shrink-0 w-8 h-8 bg-primary/10 rounded-md flex items-center justify-center text-primary" >

< i


class ="fa-solid fa-play" > < / i >

< / div >
< div


class ="ml-3 flex-1" >

< p


class ="font-medium" > 1.1 课程介绍与环境搭建 < / p >

< p


class ="text-xs text-gray-500" > 25分钟 < / p >

< / div >
< div


class ="flex-shrink-0" >

< span


class ="text-xs bg-green-100 text-green-600 px-2 py-1 rounded-full" > 已完成 < / span >

< / div >
< / div >
< div


class ="flex items-center p-2 hover:bg-gray-50 rounded-lg transition-colors" >

< div


class ="flex-shrink-0 w-8 h-8 bg-primary/10 rounded-md flex items-center justify-center text-primary" >

< i


class ="fa-solid fa-play" > < / i >

< / div >
< div


class ="ml-3 flex-1" >

< p


class ="font-medium" > 1.2 变量与数据类型 < / p >

< p


class ="text-xs text-gray-500" > 30分钟 < / p >

< / div >
< div


class ="flex-shrink-0" >

< span


class ="text-xs bg-green-100 text-green-600 px-2 py-1 rounded-full" > 已完成 < / span >

< / div >
< / div >
< div


class ="flex items-center p-2 hover:bg-gray-50 rounded-lg transition-colors" >

< div


class ="flex-shrink-0 w-8 h-8 bg-primary/10 rounded-md flex items-center justify-center text-primary" >

< i


class ="fa-solid fa-play" > < / i >

< / div >
< div


class ="ml-3 flex-1" >

< p


class ="font-medium" > 1.3 条件语句与循环 < / p >

< p


class ="text-xs text-gray-500" > 40分钟 < / p >

< / div >
< div


class ="flex-shrink-0" >

< span


class ="text-xs bg-yellow-100 text-yellow-600 px-2 py-1 rounded-full" > 进行中 < / span >

< / div >
< / div >
< div


class ="flex items-center p-2 hover:bg-gray-50 rounded-lg transition-colors" >

< div


class ="flex-shrink-0 w-8 h-8 bg-gray-100 rounded-md flex items-center justify-center text-gray-400" >

< i


class ="fa-solid fa-lock" > < / i >

< / div >
< div


class ="ml-3 flex-1" >

< p


class ="font-medium" > 1.4 函数与模块 < / p >

< p


class ="text-xs text-gray-500" > 35分钟 < / p >

< / div >
< div


class ="flex-shrink-0" >

< span


class ="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full" > 未开始 < / span >

< / div >
< / div >
< / div >
< / div >

< !-- 章节2 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden" >

< div


class ="bg-neutral px-4 py-3 flex justify-between items-center cursor-pointer" >

< div


class ="flex items-center" >

< i


class ="fa-solid fa-chevron-right text-gray-500 mr-3 transition-transform" > < / i >

< h4


class ="font-medium" > 第2章 数据结构 < / h4 >

< / div >
< div


class ="text-xs text-gray-500" > 5课时 < / div >

< / div >
< div


class ="p-4 space-y-3 bg-white hidden" >

< !-- 章节2内容，默认隐藏 -->
< / div >
< / div >

< !-- 章节3 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden" >

< div


class ="bg-neutral px-4 py-3 flex justify-between items-center cursor-pointer" >

< div


class ="flex items-center" >

< i


class ="fa-solid fa-chevron-right text-gray-500 mr-3 transition-transform" > < / i >

< h4


class ="font-medium" > 第3章 文件操作与异常处理 < / h4 >

< / div >
< div


class ="text-xs text-gray-500" > 4课时 < / div >

< / div >
< div


class ="p-4 space-y-3 bg-white hidden" >

< !-- 章节3内容，默认隐藏 -->
< / div >
< / div >

< !-- 章节4 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden" >

< div


class ="bg-neutral px-4 py-3 flex justify-between items-center cursor-pointer" >

< div


class ="flex items-center" >

< i


class ="fa-solid fa-chevron-right text-gray-500 mr-3 transition-transform" > < / i >

< h4


class ="font-medium" > 第4章 面向对象编程 < / h4 >

< / div >
< div


class ="text-xs text-gray-500" > 6课时 < / div >

< / div >
< div


class ="p-4 space-y-3 bg-white hidden" >

< !-- 章节4内容，默认隐藏 -->
< / div >
< / div >
< / div >
< / div >

< div


class ="border-t border-gray-200 pt-6" >

< h3


class ="text-lg font-semibold mb-4" > 学习进度 < / h3 >

< div


class ="bg-gray-100 rounded-full h-2.5 mb-4" >

< div


class ="bg-primary h-2.5 rounded-full" style="width: 25%" > < / div >

< / div >
< div


class ="flex justify-between text-sm text-gray-600" >

< span > 已完成: 7 / 28
课时 < / span >
< span > 预计完成时间: 2025 - 06 - 30 < / span >
< / div >
< / div >
< / div >

< !-- 课件内容 -->
< div
id = "课件"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 互动课件 < / h3 >

< div


class ="flex items-center space-x-2" >

< div


class ="relative" >

< input
type = "text"
placeholder = "搜索课件..."


class ="pl-8 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all text-sm" >

< i


class ="fa-solid fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" > < / i >

< / div >
< select


class ="border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary" >

< option > 全部类型 < / option >
< option > PPT < / option >
< option > PDF < / option >
< option > 视频 < / option >
< option > 代码示例 < / option >
< / select >
< / div >
< / div >

< div


class ="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" >

< !-- 课件卡片1 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden hover:shadow-md transition-shadow" >

< div


class ="bg-neutral h-40 flex items-center justify-center" >

< i


class ="fa-regular fa-file-powerpoint text-6xl text-primary/30" > < / i >

< / div >
< div


class ="p-4" >

< h4


class ="font-medium mb-1" > Python基础语法 < / h4 >

< p


class ="text-sm text-gray-500 mb-3" > 介绍Python的基本语法和编程规范 < / p >

< div


class ="flex justify-between items-center" >

< div


class ="text-xs text-gray-500" >

< i


class ="fa-regular fa-file-powerpoint mr-1" > < / i > PPT

< / div >
< div


class ="flex space-x-2" >

< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-download" > < / i >

< / button >
< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-eye" > < / i >

< / button >
< / div >
< / div >
< / div >
< / div >

< !-- 课件卡片2 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden hover:shadow-md transition-shadow" >

< div


class ="bg-neutral h-40 flex items-center justify-center" >

< i


class ="fa-regular fa-file-pdf text-6xl text-red-300" > < / i >

< / div >
< div


class ="p-4" >

< h4


class ="font-medium mb-1" > 变量与数据类型详解 < / h4 >

< p


class ="text-sm text-gray-500 mb-3" > 深入理解Python中的各种数据类型 < / p >

< div


class ="flex justify-between items-center" >

< div


class ="text-xs text-gray-500" >

< i


class ="fa-regular fa-file-pdf mr-1" > < / i > PDF

< / div >
< div


class ="flex space-x-2" >

< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-download" > < / i >

< / button >
< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-eye" > < / i >

< / button >
< / div >
< / div >
< / div >
< / div >

< !-- 课件卡片3 -->
< div


class ="border border-gray-200 rounded-lg overflow-hidden hover:shadow-md transition-shadow" >

< div


class ="bg-neutral h-40 flex items-center justify-center" >

< i


class ="fa-regular fa-file-code text-6xl text-green-300" > < / i >

< / div >
< div


class ="p-4" >

< h4


class ="font-medium mb-1" > 条件语句与循环示例 < / h4 >

< p


class ="text-sm text-gray-500 mb-3" > Python中条件和循环的各种应用示例 < / p >

< div


class ="flex justify-between items-center" >

< div


class ="text-xs text-gray-500" >

< i


class ="fa-regular fa-file-code mr-1" > < / i > 代码文件

< / div >
< div


class ="flex space-x-2" >

< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-download" > < / i >

< / button >
< button


class ="text-gray-500 hover:text-primary transition-colors" >

< i


class ="fa-solid fa-code" > < / i >

< / button >
< / div >
< / div >
< / div >
< / div >
< / div >
< / div >
< / div >

< !-- 作业内容 -->
< div
id = "作业"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 作业 < / h3 >

< button


class ="bg-primary/10 text-primary px-3 py-1.5 rounded-lg text-sm hover:bg-primary/20 transition-colors" >

< i


class ="fa-solid fa-plus mr-1" > < / i > 提交作业

< / button >
< / div >

< div


class ="overflow-x-auto" >

< table


class ="min-w-full divide-y divide-gray-200" >

< thead >
< tr >
< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 作业名称 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 发布时间 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 截止时间 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 状态 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 操作 < / th >

< / tr >
< / thead >
< tbody


class ="bg-white divide-y divide-gray-200" >

< tr >
< td


class ="px-6 py-4 whitespace-nowrap" >

< div


class ="text-sm font-medium text-gray-900" > Python基础语法练习 < / div >

< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 05 - 01
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 05 - 15
< / td >
< td


class ="px-6 py-4 whitespace-nowrap" >

< span


class ="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800" >


待提交
< / span >
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >

< a
href = "#"


class ="text-primary hover:text-primary/80" > 查看详情 < / a >

< / td >
< / tr >
< tr >
< td


class ="px-6 py-4 whitespace-nowrap" >

< div


class ="text-sm font-medium text-gray-900" > 数据类型与变量作业 < / div >

< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 04 - 20
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 04 - 30
< / td >
< td


class ="px-6 py-4 whitespace-nowrap" >

< span


class ="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800" >


已提交
< / span >
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >

< a
href = "#"


class ="text-primary hover:text-primary/80" > 查看详情 < / a >

< / td >
< / tr >
< tr >
< td


class ="px-6 py-4 whitespace-nowrap" >

< div


class ="text-sm font-medium text-gray-900" > Python编程小项目 < / div >

< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 04 - 10
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 04 - 25
< / td >
< td


class ="px-6 py-4 whitespace-nowrap" >

< span


class ="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800" >


已批改
< / span >
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >

< a
href = "#"


class ="text-primary hover:text-primary/80" > 查看详情 < / a >

< / td >
< / tr >
< / tbody >
< / table >
< / div >
< / div >
< / div >

< !-- 测试内容 -->
< div
id = "测试"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 测试 < / h3 >

< button


class ="bg-primary/10 text-primary px-3 py-1.5 rounded-lg text-sm hover:bg-primary/20 transition-colors" >

< i


class ="fa-solid fa-plus mr-1" > < / i > 开始测试

< / button >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5 mb-4" >

< div


class ="flex justify-between items-start mb-4" >

< div >
< h4


class ="font-medium text-lg mb-1" > 第1章 Python基础测试 < / h4 >

< p


class ="text-sm text-gray-500" > 本测试涵盖变量、数据类型、条件语句和循环等内容 < / p >

< / div >
< span


class ="bg-yellow-100 text-yellow-800 text-xs font-medium px-2.5 py-0.5 rounded-full" >


即将截止
< / span >
< / div >
< div


class ="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4" >

< div


class ="bg-gray-50 p-3 rounded-lg" >

< p


class ="text-sm text-gray-500 mb-1" > 题目数量 < / p >

< p


class ="font-medium" > 20题 < / p >

< / div >
< div


class ="bg-gray-50 p-3 rounded-lg" >

< p


class ="text-sm text-gray-500 mb-1" > 考试时长 < / p >

< p


class ="font-medium" > 60分钟 < / p >

< / div >
< div


class ="bg-gray-50 p-3 rounded-lg" >

< p


class ="text-sm text-gray-500 mb-1" > 截止日期 < / p >

< p


class ="font-medium" > 2025-05-15 < / p >

< / div >
< / div >
< div


class ="flex justify-between items-center" >

< div


class ="text-sm text-gray-500" >

< i


class ="fa-regular fa-clock mr-1" > < / i > 剩余时间: 3


天5小时
< / div >
< button


class ="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded-lg transition-all" >


开始测试
< / button >
< / div >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5" >

< div


class ="flex justify-between items-start mb-4" >

< div >
< h4


class ="font-medium text-lg mb-1" > Python编程入门摸底测试 < / h4 >

< p


class ="text-sm text-gray-500" > 评估你的Python基础知识水平 < / p >

< / div >
< span


class ="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full" >


已完成
< / span >
< / div >
< div


class ="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4" >

< div


class ="bg-gray-50 p-3 rounded-lg" >

< p


class ="text-sm text-gray-500 mb-1" > 得分 < / p >

< p


class ="font-medium text-green-600" > 85 / 100 < / p >

< / div >
< div


class ="bg-gray-50 p-3 rounded-lg" >

< p


class ="text-sm text-gray-500 mb-1" > 考试时长 < / p >

< p


class ="font-medium" > 45分钟 < / p >

< / div >
< div


class ="bg-gray-50 p-3 rounded-lg" >

< p


class ="text-sm text-gray-500 mb-1" > 考试日期 < / p >

< p


class ="font-medium" > 2025-04-20 < / p >

< / div >
< / div >
< div


class ="flex justify-between items-center" >

< div


class ="text-sm text-gray-500" >

< i


class ="fa-regular fa-check-circle mr-1" > < / i > 已通过

< / div >
< button


class ="bg-gray-100 hover:bg-gray-200 text-gray-700 px-4 py-2 rounded-lg transition-all" >


查看详情
< / button >
< / div >
< / div >
< / div >
< / div >

< !-- 腾讯会议内容 -->
< div
id = "会议"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 腾讯会议 < / h3 >

< button


class ="bg-primary/10 text-primary px-3 py-1.5 rounded-lg text-sm hover:bg-primary/20 transition-colors" >

< i


class ="fa-solid fa-plus mr-1" > < / i > 预约会议

< / button >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5 mb-4" >

< div


class ="flex justify-between items-center mb-4" >

< h4


class ="font-medium text-lg" > 本周直播安排 < / h4 >

< div


class ="text-sm text-gray-500" >

< i


class ="fa-regular fa-calendar mr-1" > < / i > 2025年5月第2周

< / div >
< / div >

< div


class ="space-y-4" >

< div


class ="bg-primary/5 border border-primary/20 rounded-lg p-4" >

< div


class ="flex justify-between items-start" >

< div >
< h5


class ="font-medium mb-1" > Python条件语句详解 < / h5 >

< p


class ="text-sm text-gray-600 mb-2" > 李教授 < / p >

< div


class ="flex items-center text-sm text-gray-500 mb-2" >

< i


class ="fa-regular fa-calendar mr-1" > < / i >

< span > 2025 - 05 - 13
19: 00 - 21:00 < / span >
< / div >
< div


class ="flex items-center text-sm text-gray-500" >

< i


class ="fa-solid fa-id-card mr-1" > < / i >

< span > 会议号: 876
543
210 < / span >
< / div >
< / div >
< div


class ="flex flex-col space-y-2" >

< button


class ="bg-primary hover:bg-primary/90 text-white px-3 py-1 rounded-lg text-sm transition-all" >


加入会议
< / button >
< button


class ="bg-white border border-gray-200 hover:bg-gray-50 text-gray-700 px-3 py-1 rounded-lg text-sm transition-all" >


复制会议号
< / button >
< / div >
< / div >
< / div >

< div


class ="bg-gray-50 border border-gray-200 rounded-lg p-4" >

< div


class ="flex justify-between items-start" >

< div >
< h5


class ="font-medium mb-1" > Python循环结构与应用 < / h5 >

< p


class ="text-sm text-gray-600 mb-2" > 李教授 < / p >

< div


class ="flex items-center text-sm text-gray-500 mb-2" >

< i


class ="fa-regular fa-calendar mr-1" > < / i >

< span > 2025 - 05 - 15
19: 00 - 21:00 < / span >
< / div >
< div


class ="flex items-center text-sm text-gray-500" >

< i


class ="fa-solid fa-id-card mr-1" > < / i >

< span > 会议号: 987
654
321 < / span >
< / div >
< / div >
< div


class ="flex flex-col space-y-2" >

< button


class ="bg-gray-200 text-gray-500 px-3 py-1 rounded-lg text-sm cursor-not-allowed" >


未开始
< / button >
< button


class ="bg-white border border-gray-200 hover:bg-gray-50 text-gray-700 px-3 py-1 rounded-lg text-sm transition-all" >


复制会议号
< / button >
< / div >
< / div >
< / div >

< div


class ="bg-gray-50 border border-gray-200 rounded-lg p-4" >

< div


class ="flex justify-between items-start" >

< div >
< h5


class ="font-medium mb-1" > 函数与模块编程实践 < / h5 >

< p


class ="text-sm text-gray-600 mb-2" > 李教授 < / p >

< div


class ="flex items-center text-sm text-gray-500 mb-2" >

< i


class ="fa-regular fa-calendar mr-1" > < / i >

< span > 2025 - 05 - 17
10: 00 - 12:00 < / span >
< / div >
< div


class ="flex items-center text-sm text-gray-500" >

< i


class ="fa-solid fa-id-card mr-1" > < / i >

< span > 会议号: 765
432
109 < / span >
< / div >
< / div >
< div


class ="flex flex-col space-y-2" >

< button


class ="bg-gray-200 text-gray-500 px-3 py-1 rounded-lg text-sm cursor-not-allowed" >


未开始
< / button >
< button


class ="bg-white border border-gray-200 hover:bg-gray-50 text-gray-700 px-3 py-1 rounded-lg text-sm transition-all" >


复制会议号
< / button >
< / div >
< / div >
< / div >
< / div >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5" >

< h4


class ="font-medium text-lg mb-4" > 往期会议记录 < / h4 >

< div


class ="overflow-x-auto" >

< table


class ="min-w-full divide-y divide-gray-200" >

< thead >
< tr >
< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 会议主题 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 时间 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 主持人 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 会议号 < / th >

< th


class ="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" > 操作 < / th >

< / tr >
< / thead >
< tbody


class ="bg-white divide-y divide-gray-200" >

< tr >
< td


class ="px-6 py-4 whitespace-nowrap" >

< div


class ="text-sm font-medium text-gray-900" > 课程介绍与环境搭建 < / div >

< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 04 - 20
19: 00
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


李教授
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


123
456
789
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >

< a
href = "#"


class ="text-primary hover:text-primary/80" > 查看回放 < / a >

< / td >
< / tr >
< tr >
< td


class ="px-6 py-4 whitespace-nowrap" >

< div


class ="text-sm font-medium text-gray-900" > 变量与数据类型详解 < / div >

< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


2025 - 04 - 22
19: 00
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


李教授
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >


234
567
890
< / td >
< td


class ="px-6 py-4 whitespace-nowrap text-sm text-gray-500" >

< a
href = "#"


class ="text-primary hover:text-primary/80" > 查看回放 < / a >

< / td >
< / tr >
< / tbody >
< / table >
< / div >
< / div >
< / div >
< / div >

< !-- 公告内容 -->
< div
id = "公告"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 公告 < / h3 >

< div


class ="text-sm text-gray-500" >


共 < span


class ="font-medium" > 5 < / span > 条公告

< / div >
< / div >

< div


class ="space-y-4" >

< div


class ="bg-white rounded-lg border border-gray-200 p-5 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-start mb-3" >

< h4


class ="font-medium text-lg" > 课程进度安排调整通知 < / h4 >

< span


class ="bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full" >


重要
< / span >
< / div >
< p


class ="text-gray-600 mb-4" > 各位同学，由于五一假期的影响，原定于5月3日的课程将顺延至5月4日进行，请大家注意调整学习计划。另外，第1章的测试时间将延长至5月15日，请尚未完成的同学抓紧时间。 < / p >

< div


class ="flex justify-between items-center text-sm text-gray-500" >

< span > 发布时间: 2025 - 05 - 01 < / span >
< span > 发布者: 李教授 < / span >
< / div >

< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-start mb-3" >

< h4


class ="font-medium text-lg" > 关于Python编程作业的提交说明 < / h4 >

< span


class ="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full" >


通知
< / span >
< / div >
< p


class ="text-gray-600 mb-4" > 各位同学，Python编程作业需要以.py文件形式提交，请确保代码能够正常运行，并且包含必要的注释。作业提交截止后将自动关闭提交通道，请大家按时完成。 < / p >

< div


class ="flex justify-between items-center text-sm text-gray-500" >

< span > 发布时间: 2025 - 04 - 28 < / span >
< span > 发布者: 李教授 < / span >
< / div >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-start mb-3" >

< h4


class ="font-medium text-lg" > 补充学习资料发布 < / h4 >

< span


class ="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full" >


资源
< / span >
< / div >
< p


class ="text-gray-600 mb-4" > 已在"互动课件"板块上传了《Python编程从入门到精通》的补充学习资料，包含更多的代码示例和练习题，供有需要的同学参考学习。 < / p >

< div


class ="flex justify-between items-center text-sm text-gray-500" >

< span > 发布时间: 2025 - 04 - 25 < / span >
< span > 发布者: 李教授 < / span >
< / div >
< / div >
< / div >
< / div >
< / div >

< !-- 话题内容 -->
< div
id = "话题"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 话题讨论 < / h3 >

< button


class ="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded-lg transition-all" >

< i


class ="fa-solid fa-pencil mr-1" > < / i > 发布话题

< / button >
< / div >

< div


class ="border border-gray-200 rounded-lg overflow-hidden" >

< div


class ="bg-gray-50 px-4 py-3 flex items-center justify-between" >

< div


class ="flex items-center space-x-4" >

< button


class ="text-primary font-medium" > 全部 < / button >

< button


class ="text-gray-500 hover:text-primary" > 精华 < / button >

< button


class ="text-gray-500 hover:text-primary" > 已解决 < / button >

< button


class ="text-gray-500 hover:text-primary" > 未解决 < / button >

< / div >
< div


class ="flex items-center" >

< div


class ="relative" >

< input
type = "text"
placeholder = "搜索话题..."


class ="pl-8 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all text-sm" >

< i


class ="fa-solid fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" > < / i >

< / div >
< / div >
< / div >

< div


class ="divide-y divide-gray-200" >

< !-- 话题1 -->
< div


class ="p-4 hover:bg-gray-50 transition-colors" >

< div


class ="flex items-start" >

< div


class ="flex-shrink-0 mr-3" >

< img


class ="h-10 w-10 rounded-full" src="https://picsum.photos/seed/user1/100/100" alt="用户头像" >

< / div >
< div


class ="flex-1" >

< div


class ="flex justify-between items-start" >

< h4


class ="font-medium text-gray-900 hover:text-primary" > Python中列表和元组的区别是什么？ < / h4 >

< span


class ="text-xs text-gray-500" > 2小时前 < / span >

< / div >
< p


class ="text-sm text-gray-600 mt-1 mb-2" > 刚学习Python，对列表和元组的概念有点混淆，它们之间的主要区别是什么？在什么情况下应该选择使用列表或元组？ < / p >

< div


class ="flex justify-between items-center" >

< div


class ="flex items-center space-x-4 text-sm text-gray-500" >

< div


class ="flex items-center" >

< i


class ="fa-regular fa-user mr-1" > < / i >

< span > 张三 < / span >
< / div >
< div


class ="flex items-center" >

< i


class ="fa-regular fa-comment mr-1" > < / i >

< span > 12 < / span >
< / div >
< div


class ="flex items-center" >

< i


class ="fa-regular fa-eye mr-1" > < / i >

< span > 128 < / span >
< / div >
< / div >
< div


class ="flex items-center space-x-2" >

< span


class ="bg-green-100 text-green-800 text-xs font-medium px-2 py-0.5 rounded-full" > 已解决 < / span >

< span


class ="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-0.5 rounded-full" > 基础 < / span >

< / div >
< / div >
< / div >
< / div >
< / div >

< !-- 话题2 -->
< div


class ="p-4 hover:bg-gray-50 transition-colors" >

< div


class ="flex items-start" >

< div


class ="flex-shrink-0 mr-3" >

< img


class ="h-10 w-10 rounded-full" src="https://picsum.photos/seed/user2/100/100" alt="用户头像" >

< / div >
< div


class ="flex-1" >

< div


class ="flex justify-between items-start" >

< h4


class ="font-medium text-gray-900 hover:text-primary" > 关于条件语句的一个小问题 < / h4 >

< span


class ="text-xs text-gray-500" > 昨天 < / span >

< / div >
< p


class ="text-sm text-gray-600 mt-1 mb-2" > 下面这段代码为什么总是输出"条件不满足"？我已经检查过变量值是符合条件的。 < / p >

< div


class ="bg-gray-100 p-3 rounded-lg mb-2" >

< pre


class ="text-xs text-gray-800 font-mono" > x = 5


if x = 5:
    print("条件满足")
else:
    print("条件不满足") < / pre >
    < / div >
    < div


    class ="flex justify-between items-center" >

    < div


    class ="flex items-center space-x-4 text-sm text-gray-500" >

    < div


    class ="flex items-center" >

    < i


    class ="fa-regular fa-user mr-1" > < / i >

    < span > 李四 < / span >
< / div >
< div


class ="flex items-center" >

< i


class ="fa-regular fa-comment mr-1" > < / i >

< span > 8 < / span >
< / div >
< div


class ="flex items-center" >

< i


class ="fa-regular fa-eye mr-1" > < / i >

< span > 95 < / span >
< / div >
< / div >
< div


class ="flex items-center space-x-2" >

< span


class ="bg-yellow-100 text-yellow-800 text-xs font-medium px-2 py-0.5 rounded-full" > 未解决 < / span >

< span


class ="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-0.5 rounded-full" > 基础 < / span >

< / div >
< / div >
< / div >
< / div >
< / div >

< !-- 话题3 -->
< div


class ="p-4 hover:bg-gray-50 transition-colors" >

< div


class ="flex items-start" >

< div


class ="flex-shrink-0 mr-3" >

< img


class ="h-10 w-10 rounded-full" src="https://picsum.photos/seed/user3/100/100" alt="用户头像" >

< / div >
< div


class ="flex-1" >

< div


class ="flex justify-between items-start" >

< h4


class ="font-medium text-gray-900 hover:text-primary" > 推荐一些Python学习资源 < / h4 >

< span


class ="text-xs text-gray-500" > 3天前 < / span >

< / div >
< p


class ="text-sm text-gray-600 mt-1 mb-2" > 除了课程提供的资料外，大家有没有其他推荐的Python学习资源？书籍、网站或者视频教程都可以。 < / p >

< div


class ="flex justify-between items-center" >

< div


class ="flex items-center space-x-4 text-sm text-gray-500" >

< div


class ="flex items-center" >

< i


class ="fa-regular fa-user mr-1" > < / i >

< span > 王五 < / span >
< / div >
< div


class ="flex items-center" >

< i


class ="fa-regular fa-comment mr-1" > < / i >

< span > 23 < / span >
< / div >
< div


class ="flex items-center" >

< i


class ="fa-regular fa-eye mr-1" > < / i >

< span > 210 < / span >
< / div >
< / div >
< div


class ="flex items-center space-x-2" >

< span


class ="bg-purple-100 text-purple-800 text-xs font-medium px-2 py-0.5 rounded-full" > 讨论 < / span >

< / div >
< / div >
< / div >
< / div >
< / div >
< / div >

< div


class ="bg-gray-50 px-4 py-3 flex items-center justify-between" >

< div


class ="text-sm text-gray-500" >


显示
1 - 3
条，共
15
条
< / div >
< div


class ="flex space-x-1" >

< button


class ="w-8 h-8 flex items-center justify-center rounded border border-gray-200 text-gray-500 hover:border-primary hover:text-primary disabled:opacity-50 disabled:cursor-not-allowed" disabled >

< i


class ="fa-solid fa-chevron-left text-xs" > < / i >

< / button >
< button


class ="w-8 h-8 flex items-center justify-center rounded border border-primary bg-primary text-white" > 1 < / button >

< button


class ="w-8 h-8 flex items-center justify-center rounded border border-gray-200 hover:border-primary hover:text-primary" > 2 < / button >

< button


class ="w-8 h-8 flex items-center justify-center rounded border border-gray-200 hover:border-primary hover:text-primary" > 3 < / button >

< button


class ="w-8 h-8 flex items-center justify-center rounded border border-gray-200 text-gray-500 hover:border-primary hover:text-primary" >

< i


class ="fa-solid fa-chevron-right text-xs" > < / i >

< / button >
< / div >
< / div >
< / div >
< / div >
< / div >

< !-- 互动答题内容 -->
< div
id = "答题"


class ="tab-content" >

< div


class ="mb-6" >

< div


class ="flex justify-between items-center mb-4" >

< h3


class ="text-lg font-semibold" > 互动答题 < / h3 >

< div


class ="flex items-center space-x-2" >

< select


class ="border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary" >

< option > 全部类型 < / option >
< option > 单选题 < / option >
< option > 多选题 < / option >
< option > 判断题 < / option >
< option > 编程题 < / option >
< / select >
< select


class ="border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary" >

< option > 难度不限 < / option >
< option > 初级 < / option >
< option > 中级 < / option >
< option > 高级 < / option >
< / select >
< / div >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5 mb-4" >

< div


class ="flex justify-between items-center mb-4" >

< h4


class ="font-medium" > 今日答题挑战 < / h4 >

< span


class ="text-sm text-gray-500" >

< i


class ="fa-regular fa-clock mr-1" > < / i > 剩余时间: 12


小时30分钟
< / span >
< / div >

< div


class ="mb-4" >

< p


class ="text-sm font-medium mb-2" > 1. 以下哪个是Python的内置数据类型？ < / p >

< div


class ="space-y-2" >

< div


class ="flex items-center p-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer" >

< div


class ="w-5 h-5 rounded-full border border-gray-300 mr-3 flex-shrink-0" > < / div >

< span > A.数组(Array) < / span >
< / div >
< div


class ="flex items-center p-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer" >

< div


class ="w-5 h-5 rounded-full border border-gray-300 mr-3 flex-shrink-0" > < / div >

< span > B.列表(List) < / span >
< / div >
< div


class ="flex items-center p-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer" >

< div


class ="w-5 h-5 rounded-full border border-gray-300 mr-3 flex-shrink-0" > < / div >

< span > C.字典(Dictionary) < / span >
< / div >
< div


class ="flex items-center p-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer" >

< div


class ="w-5 h-5 rounded-full border border-gray-300 mr-3 flex-shrink-0" > < / div >

< span > D.以上都是 < / span >
< / div >
< / div >
< / div >

< div


class ="flex justify-between items-center" >

< button


class ="bg-gray-200 text-gray-500 px-4 py-2 rounded-lg cursor-not-allowed" > 上一题 < / button >

< button


class ="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded-lg transition-all" > 下一题 < / button >

< / div >
< / div >

< div


class ="bg-white rounded-lg border border-gray-200 p-5" >

< h4


class ="font-medium mb-4" > 热门题库 < / h4 >

< div


class ="grid grid-cols-1 md:grid-cols-2 gap-4" >

< div


class ="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-center mb-3" >

< h5


class ="font-medium" > Python基础语法 < / h5 >

< span


class ="text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full" > 100题 < / span >

< / div >
< p


class ="text-sm text-gray-600 mb-3" > 涵盖变量、数据类型、条件语句、循环等基础语法知识 < / p >

< div


class ="flex justify-between items-center text-sm" >

< div


class ="text-gray-500" >

< i


class ="fa-regular fa-user mr-1" > < / i > 1, 234人已练习

< / div >
< button


class ="text-primary hover:text-primary/80" > 开始练习 < / button >

< / div >
< / div >

< div


class ="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-center mb-3" >

< h5


class ="font-medium" > 函数与模块 < / h5 >

< span


class ="text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full" > 85题 < / span >

< / div >
< p


class ="text-sm text-gray-600 mb-3" > 关于函数定义、参数传递、模块导入等相关知识 < / p >

< div


class ="flex justify-between items-center text-sm" >

< div


class ="text-gray-500" >

< i


class ="fa-regular fa-user mr-1" > < / i > 987人已练习

< / div >
< button


class ="text-primary hover:text-primary/80" > 开始练习 < / button >

< / div >
< / div >

< div


class ="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-center mb-3" >

< h5


class ="font-medium" > 面向对象编程 < / h5 >

< span


class ="text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full" > 120题 < / span >

< / div >
< p


class ="text-sm text-gray-600 mb-3" > 类、对象、继承、多态等面向对象编程的概念和应用 < / p >

< div


class ="flex justify-between items-center text-sm" >

< div


class ="text-gray-500" >

< i


class ="fa-regular fa-user mr-1" > < / i > 876人已练习

< / div >
< button


class ="text-primary hover:text-primary/80" > 开始练习 < / button >

< / div >
< / div >

< div


class ="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow" >

< div


class ="flex justify-between items-center mb-3" >

< h5


class ="font-medium" > 文件操作与异常处理 < / h5 >

< span


class ="text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full" > 75题 < / span >

< / div >
< p


class ="text-sm text-gray-600 mb-3" > 文件读写、异常捕获与处理等相关知识 < / p >

< div


class ="flex justify-between items-center text-sm" >

< div


class ="text-gray-500" >

< i


class ="fa-regular fa-user mr-1" > < / i > 765人已练习

< / div >
< button


class ="text-primary hover:text-primary/80" > 开始练习