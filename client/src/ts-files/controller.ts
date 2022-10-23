(function () {
  let model = new Model();
  let renderer = new Renderer();

  $("#search-btn").on("click", function () {
    const gluten = $("#gluten").prop("checked");
    const dairy = $("#dairy").prop("checked");
    const ingredient = $("#ingredient").val();
    model.fetchRecipes(ingredient, dairy, gluten).then(function (res) {
      renderer.render(model.getRecipes());
      $("#ingredient").val("");
    });
  });

  $(".recipes-container").on("click", ".recipe-img", function () {
    const firstIngredient = $(this).closest(".recipe").find("li:first").html();
    alert(firstIngredient);
  });
})();
