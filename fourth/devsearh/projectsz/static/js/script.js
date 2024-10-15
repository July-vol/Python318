let searchForm = document.getElementById('search');
let pageLinks = document.querySelectorAll('.page-link');

if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault();

      let page = this.dataset.page;

      searchForm.innerHTML += `<input value=${page} name="page" type="hidden" >`;

      searchForm.submit();
    })
  }
}