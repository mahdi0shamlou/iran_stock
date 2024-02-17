!(function (NioApp, $) {
    "use strict";

    // Variable
    var $win = $(window), $body = $('body'), breaks = NioApp.Break;

    NioApp.Kanban = function () {

        function titletemplate(title, count, optionicon = "more-h") {
            return (`
                <div class="kanban-title-content">
                    <h6 class="title">${title}</h6>
                    <span class="badge rounded-pill bg-outline-light text-dark">${count}</span>
                </div>
                <div class="kanban-title-content">
                    <div class="drodown">
                        <a href="#" class="dropdown-toggle btn btn-sm btn-icon btn-trigger me-n1" data-bs-toggle="dropdown"><em class="icon ni ni-${optionicon}"></em></a>
                        <div class="dropdown-menu dropdown-menu-end">
                            <ul class="link-list-opt no-bdr">
                                <li><a href="#"><em class="icon ni ni-edit"></em><span>ویرایش تابلو</span></a></li>
                                <li><a href="#"><em class="icon ni ni-plus-sm"></em><span>افزودن مسئولیت</span></a></li>
                                <li><a href="#"><em class="icon ni ni-plus-sm"></em><span>افزودن گزینه</span></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            `)
        }

        var kanban = new jKanban({
            element: '#kanban',
            gutter: '0',
            widthBoard: '320px',
            responsivePercentage: false,
            boards: [
                {
                    'id': '_open',
                    'title': titletemplate("باز", "3"),
                    'class': 'kanban-light',
                    'item': [{
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">به روز رسانی کیت طراحی دش‌لایت</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-primary"><span>ف</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-primary">
                                                        <span>ف‌ت</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">فرشید ترنیان</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>به روز رسانی طراحی رابط کاربری جدید برای قالب @dashlite بر اساس بازخوردها.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-info">دش‌لایت</span></li>
                                <li><span class="badge bg-warning">طراحی رابط کاربری</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li class="text-danger"><em class="icon ni ni-calendar"></em><span>زمان تحویل 2 روزه</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>طراحی</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>1</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>4</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }, {
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">پیاده سازی طراحی در قالب</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-dark"><span>س</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-dark">
                                                        <span>س‌د</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">ساناز درویشی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>شروع اجرای طرح جدید در کدنویسی @dashlite.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-info">دش‌لایت</span></li>
                                <li><span class="badge bg-danger">HTML</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li><em class="icon ni ni-calendar"></em><span>12 آبان 1402</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>فرانت اند</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>2</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }, {
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">نسخه ری اکت دش‌لایت</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-blue"><span>ح</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-blue">
                                                        <span>ح‌ت</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">حمیدرضا توکلی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>طراحی رابط کاربری جدید نسخه ری اکت قالب @dashlite در اسرع وقت.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-info">دش‌لایت</span></li>
                                <li><span class="badge bg-secondary">ری اکت</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li><em class="icon ni ni-calendar"></em><span>زمان تحویل 5 روزه</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>فرانت اند</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>3</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>5</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }]
                },
                {
                    'id': '_in_progress',
                    'title': titletemplate("در حال پیشرفت", "4"),
                    'class': 'kanban-primary',
                    'item': [{
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">تحقیق کلمات کلیدی techyspec</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-danger"><span>ن</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-danger">
                                                        <span>ن‌ح</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">نیوشا حقی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>تحقیق کلمات کلیدی برای پروفایل تجاری @techyspec و سایر وب سایت ها، برای بهبود رتبه.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-dark">Techyspec</span></li>
                                <li><span class="badge bg-success">سئو</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li><em class="icon ni ni-calendar"></em><span>02 مهر 1402</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>تحقیق</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>31</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>21</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    },
                    {
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">طراحی وب سایت فیتنس نکست</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-pink"><span>م</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-pink">
                                                        <span>م‌ح</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">مصطفی حجازی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>طراحی یک وب سایت عالی برای راه اندازی محصول جدید @fitness_next.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-primary">فیتنس نکست</span></li>
                                <li><span class="badge bg-warning">طراحی رابط کاربری</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li><em class="icon ni ni-calendar"></em><span>زمان تحویل 8 روزه</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>طراحی</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>3</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>5</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }, {
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">طراحی مجدد وب سایت رانرژی</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-purple">
                                                <span>ش</span>
                                            </div>
                                            <div class="user-avatar xs bg-success">
                                                <span>م</span>
                                            </div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-purple">
                                                        <span>ش‌م</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">شقایق مولوی</span>
                                                    </div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-success">
                                                        <span>م‌م</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">مهرداد موسوی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>طراحی دوباره وب سایت قدیمی و تاریخ گذشته به یک وب سایت مدرن و تمیز، با در نظر گرفتن مینیمالیسم.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-gray">طراحی مجدد</span></li>
                                <li><span class="badge bg-primary">رانرژی</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li><em class="icon ni ni-calendar"></em><span>10 مهر 1402</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>طراحی</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>12</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>8</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }, {
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">اپلیکیشن اندروید Wordlab</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-primary"><span>ش</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-primary">
                                                        <span>ش‌م</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">شقایق مولوی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>اپلیکیشن اندروید Wordlab با ری اکت نیتیو.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-success">Wordlab</span></li>
                                <li><span class="badge bg-light">اندروید</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li><em class="icon ni ni-calendar"></em><span>21 مهر 1402</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>اپلیکیشن</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>8</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>85</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }]
                },
                {
                    'id': '_to_review',
                    'title': titletemplate("برای بازبینی", "2"),
                    'class': 'kanban-warning',
                    'item': [{
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">توسعه Oberlo</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-purple">
                                                <span>ف</span>
                                            </div>
                                            <div class="user-avatar xs bg-success">
                                                <span>ی</span>
                                            </div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-primary">
                                                        <span>ف‌ت</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">فرشید ترنیان</span>
                                                    </div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-success">
                                                        <span>ی‌ا</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">یاور آقایی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>توسعه کامل وب سایت برای Oberlo - محدود شده.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-info">Oberlo</span></li>
                                <li><span class="badge bg-danger">توسعه</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li class="text-danger"><em class="icon ni ni-calendar"></em><span>زمان تحویل 1 روزه</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>بک اند</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>16</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>25</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }, {
                        'title': `
                            <div class="kanban-item-title">
                                <h6 class="title">اپلیکیشن IOS برای Getsocio</h6>
                                <div class="drodown">
                                    <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
                                        <div class="user-avatar-group">
                                            <div class="user-avatar xs bg-pink"><span>م</span></div>
                                        </div>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-end">
                                        <ul class="link-list-opt no-bdr p-3 g-2">
                                            <li>
                                                <div class="user-card">
                                                    <div class="user-avatar sm bg-pink">
                                                        <span>م‌ح</span>
                                                    </div>
                                                    <div class="user-name">
                                                        <span class="tb-lead">مصطفی حجازی</span>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="kanban-item-text">
                                <p>طراحی و توسعه اپلیکیشن Getsocio برای نسخه IOS.</p>
                            </div>
                            <ul class="kanban-item-tags">
                                <li><span class="badge bg-dark">Getsocio</span></li>
                                <li><span class="badge bg-light">IOS</span></li>
                            </ul>
                            <div class="kanban-item-meta">
                                <ul class="kanban-item-meta-list">
                                    <li class="text-danger"><em class="icon ni ni-calendar"></em><span>زمان تحویل 4 روزه</span></li>
                                    <li><em class="icon ni ni-notes"></em><span>فرانت اند</span></li>
                                </ul>
                                <ul class="kanban-item-meta-list">
                                    <li><span>3</span><em class="icon ni ni-clip"></em></li>
                                    <li><span>5</span><em class="icon ni ni-comments"></em></li>
                                </ul>
                            </div>
                        `,
                    }]
                },
                {
                    'id': '_completed',
                    'title': titletemplate("تکمیل شده", "0"),
                    'class': 'kanban-success',
                    'item': []
                }
            ]
        });
        for (var i = 0; i < kanban.options.boards.length; i++) {
            var board = kanban.findBoard(kanban.options.boards[i].id);
            $(board).find("footer").html(`<button class="kanban-add-task btn btn-block"><em class="icon ni ni-plus-sm"></em><span>افزودن مسئولیتی دیگر</span></button>`);
        }
    };

    NioApp.coms.docReady.push(NioApp.Kanban);

})(NioApp, jQuery);