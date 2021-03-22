function resizeGridItem(item){
grid = document.getElementsByClassName("grid")[0];
rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));
rowSpan = Math.ceil((item.querySelector('.content').getBoundingClientRect().height+rowGap)/(rowHeight+rowGap));
  item.style.gridRowEnd = "span "+rowSpan;
}

function resizeAllGridItems(){
  allItems = document.getElementsByClassName("item");
  for(x=0;x<allItems.length;x++){
    resizeGridItem(allItems[x]);
  }
  handle_likes()
}

function resizeInstance(instance){
item = instance.elements[0];
resizeGridItem(item);
}

window.onload = resizeAllGridItems();
window.addEventListener("resize", resizeAllGridItems);

allItems = document.getElementsByClassName("item");
for(x=0;x<allItems.length;x++){
imagesLoaded( allItems[x], resizeInstance);
}

var loadFile = function(event) {
	var image = document.getElementById('output');
  image.style.objectFit = "cover";
  image.style.borderRadius = "30px";
	image.src = URL.createObjectURL(event.target.files[0]);
};

function updateText(btn, newCount, verb){
  btn.text(newCount + " likes")
}

function handle_likes(){
  $('.like-btn').off('click');
  $(".like-btn").click(function(e){
  e.preventDefault()
  var this_ = $(this)
  var likeUrl = this_.attr("data-href")
  var likeCount = parseInt(this_.attr("data-likes"))
  var addLike = likeCount + 1
  var removeLike = likeCount - 1
  $.ajax({
    url: likeUrl,
    method: "get",
    data: {},
    success: function(data){
      var newLikes;
      console.log(data)
      this_.toggleClass("btn-primary")
      this_.toggleClass("btn-success")
      if (data.liked){
        newLikes = addLike
      } else {
        newLikes = removeLike
      }
      updateText(this_, newLikes)
      this_.attr("data-likes", newLikes)
    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
})
}
