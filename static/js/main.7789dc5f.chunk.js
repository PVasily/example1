(this["webpackJsonpmainapp-ui"]=this["webpackJsonpmainapp-ui"]||[]).push([[0],{29:function(e,t,c){e.exports={navig:"menu_navig__ix3wx"}},34:function(e,t,c){},35:function(e,t,c){},60:function(e,t,c){e.exports={nav:"nav_nav__2QQBk"}},61:function(e,t,c){"use strict";c.r(t);var n=c(1),a=c.n(n),s=c(26),o=c.n(s),r=(c(34),c(7)),i=c(2),l=(c(35),c(9)),j=c(10),d=c.n(j),b=c(0),h=function(e){var t=e.match,c=Object(n.useState)([]),a=Object(l.a)(c,2),s=a[0],o=a[1],i=Object(n.useState)([]),j=Object(l.a)(i,2),h=j[0],u=j[1],p=t.params.id;return Object(n.useEffect)((function(){d()({method:"GET",url:"http://localhost:8000/api/category/".concat(p,"/")}).then((function(e){o(e.data),u(e.data.posts)}))}),[p]),Object(b.jsxs)(b.Fragment,{children:["Category ",s.id,Object(b.jsxs)("p",{children:["Category name: ",Object(b.jsx)("strong",{children:s.name})]}),Object(b.jsx)("ul",{children:h.map((function(e){return Object(b.jsxs)("li",{children:[Object(b.jsx)("p",{children:e.title}),Object(b.jsx)("br",{}),Object(b.jsx)("hr",{}),Object(b.jsx)("p",{children:e.content}),Object(b.jsx)(r.b,{to:{pathname:"/posts/".concat(e.id,"/"),fromDashboard:!1},children:"\u0414\u0435\u0442\u0430\u043b\u044c\u043d\u0435\u0435..."})]},e.id)}))})]})},u=function(e){var t=e.match,c=Object(n.useState)({}),a=Object(l.a)(c,2),s=a[0],o=a[1],r=t.params.id;return Object(n.useEffect)((function(){d()({method:"GET",url:"http://localhost:8000/api/posts/".concat(r,"/")}).then((function(e){o(e.data)}))}),[r]),Object(b.jsx)(b.Fragment,{children:Object(b.jsx)("ul",{children:Object(b.jsxs)("li",{children:[Object(b.jsx)("p",{children:s.title}),Object(b.jsx)("br",{}),Object(b.jsx)("hr",{}),Object(b.jsx)("p",{children:s.content})]},s.id)})})},p=(c(60),function(){var e=Object(n.useState)([]),t=Object(l.a)(e,2),c=t[0],a=t[1];return Object(n.useEffect)((function(){d()({method:"GET",url:"http://localhost:8000/api/category/"}).then((function(e){a(e.data)}))}),[]),Object(b.jsx)(b.Fragment,{children:c.map((function(e){return Object(b.jsx)(r.b,{to:{pathname:"category/".concat(e.id,"/"),fromDashboard:!1},className:"dropdown-item",href:"#",children:e.name},e.id)}))})}),x=c(29),O=c.n(x),m=function(){return Object(b.jsx)(b.Fragment,{children:Object(b.jsx)("div",{className:O.a.navig,children:Object(b.jsxs)("ul",{children:[Object(b.jsx)("li",{children:Object(b.jsx)(r.c,{to:"/home",children:"Main"})}),Object(b.jsx)("li",{children:Object(b.jsx)(r.c,{to:"/news",children:"Goods catalog"})}),Object(b.jsx)("li",{children:Object(b.jsx)(r.c,{to:"/about",children:"About"})}),Object(b.jsx)("li",{children:Object(b.jsx)(r.c,{to:"/login",children:"Login"})}),Object(b.jsx)("li",{children:Object(b.jsx)("div",{className:"container",children:Object(b.jsxs)("div",{class:"dropdown show",children:[Object(b.jsx)("a",{className:"btn btn-secondary dropdown-toggle",href:"#",role:"button",id:"dropdownMenuLink","data-toggle":"dropdown","aria-haspopup":"true","aria-expanded":"false",children:"News"}),Object(b.jsx)("div",{className:"dropdown-menu","aria-labelledby":"dropdownMenuLink",children:Object(b.jsx)(p,{})})]})})})]})})})},f=function(){return Object(b.jsx)(b.Fragment,{children:Object(b.jsx)("div",{children:Object(b.jsx)("h3",{children:"This is home page"})})})},g=function(){var e=Object(n.useState)([]),t=Object(l.a)(e,2),c=t[0],a=t[1];Object(n.useEffect)((function(){d()({method:"GET",url:"http://localhost:8000/api/customers/"}).then((function(e){a(e.data),console.log(e.data)}))}),[]),console.log(c);var s=Object(n.useState)(""),o=Object(l.a)(s,2),r=o[0],i=o[1],j=Object(n.useState)(""),h=Object(l.a)(j,2),u=h[0],p=h[1],x="Match";return Object(b.jsxs)(b.Fragment,{children:[c.map((function(e){x=e.id==!r?"\u0415\u0441\u0442\u044c \u0441\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u0435":"\u041d\u0435 \u0441\u043e\u0432\u043f\u0430\u043b\u043e"})),x,Object(b.jsxs)("form",{children:[Object(b.jsxs)("div",{class:"form-group",children:[Object(b.jsx)("label",{for:"exampleInputEmail1",children:"Login"}),Object(b.jsx)("input",{type:"email",value:r,onChange:function(e){return function(e){var t=e.target.value;i(t),console.log(t)}(e)},class:"form-control",id:"exampleInputEmail1","aria-describedby":"emailHelp",placeholder:"Login"}),Object(b.jsx)("small",{id:"emailHelp",class:"form-text text-muted",children:"We'll never share your email with anyone else."})]}),Object(b.jsxs)("div",{class:"form-group",children:[Object(b.jsx)("label",{for:"exampleInputPassword1",children:"Password"}),Object(b.jsx)("input",{type:"password",value:u,onChange:function(e){return function(e){var t=e.target.value;p(t),console.log(t)}(e)},class:"form-control",id:"exampleInputPassword1",placeholder:"Password"})]}),Object(b.jsxs)("div",{class:"form-check",children:[Object(b.jsx)("input",{type:"checkbox",class:"form-check-input",id:"exampleCheck1"}),Object(b.jsx)("label",{class:"form-check-label",for:"exampleCheck1",children:"Check me out"})]}),Object(b.jsx)("button",{type:"button",onClick:function(){x=r==c[0].id?"\u0415\u0441\u0442\u044c \u0441\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u0435":"\u041d\u0435 \u0441\u043e\u0432\u043f\u0430\u043b\u043e"},class:"btn btn-primary",children:"Submit"})]})]})};var v=function(){return Object(b.jsxs)("div",{className:"App",children:[Object(b.jsxs)(r.a,{children:[Object(b.jsx)(m,{}),Object(b.jsxs)(i.c,{children:[Object(b.jsx)(i.a,{path:"/category/:id",exact:!0,component:h}),Object(b.jsx)(i.a,{path:"/posts/:id",exact:!0,component:u}),Object(b.jsx)(i.a,{path:"/home",exact:!0,component:f}),Object(b.jsx)(i.a,{path:"/login",exact:!0,component:g})]})]}),Object(b.jsx)("h4",{children:"Hello from React"})]})},w=function(e){e&&e instanceof Function&&c.e(3).then(c.bind(null,62)).then((function(t){var c=t.getCLS,n=t.getFID,a=t.getFCP,s=t.getLCP,o=t.getTTFB;c(e),n(e),a(e),s(e),o(e)}))};o.a.render(Object(b.jsx)(a.a.StrictMode,{children:Object(b.jsx)(v,{})}),document.getElementById("root")),w()}},[[61,1,2]]]);
//# sourceMappingURL=main.7789dc5f.chunk.js.map