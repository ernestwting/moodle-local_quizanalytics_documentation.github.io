(function () {
  var PAGES = [
    { href: "index.html", label: "Home", num: "" },
    { href: "introduction.html", label: "Introduction", num: "1" },
    { href: "getting-started.html", label: "Getting Started", num: "2" },
    { href: "installation.html", label: "Installation & Administration", num: "3" },
    { href: "using.html", label: "Using STACK q-type Analytics", num: "4" },
    { href: "calculations.html", label: "How Everything Is Calculated", num: "5" },
    { href: "privacy-security.html", label: "Privacy & Security", num: "6" },
    { href: "architecture.html", label: "Architecture & Design", num: "7" },
    { href: "glossary.html", label: "Glossary", num: "8" },
    { href: "references.html", label: "References", num: "9" }
  ];

  var here = location.pathname.split("/").pop() || "index.html";

  var brand = document.createElement("div");
  brand.className = "sb-brand";
  brand.innerHTML = "STACK q-type Analytics<small>Documentation</small>";

  var list = document.createElement("ul");
  list.className = "sb-nav";

  PAGES.forEach(function (p) {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = p.href;
    a.innerHTML = (p.num ? '<span class="sb-chnum">' + p.num + "</span>" : "") + p.label;
    if (p.href === here) a.className = "active";
    li.appendChild(a);
    list.appendChild(li);
  });

  var mount = document.getElementById("sidebar-mount");
  if (mount) {
    mount.appendChild(brand);
    mount.appendChild(list);
  }
})();
