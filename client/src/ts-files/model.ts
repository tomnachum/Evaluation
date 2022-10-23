class Recipe {
  constructor(
    public ingredients: string[],
    public title: string,
    public thumbnail: string,
    public href: string
  ) {}
}

class Model {
  private recipes: Recipe[] = [];

  private makeRequestUrl(ingredient: any, dairy: boolean, gluten: boolean) {
    let url = `/recipes?contains=${ingredient}`;
    if (dairy) {
      url += `&dairy=True`;
    }
    if (gluten) {
      url += `&gluten=True`;
    }
    console.log(url);
    return url;
  }

  async fetchRecipes(ingredient: any, dairy: boolean, gluten: boolean) {
    let url = this.makeRequestUrl(ingredient, dairy, gluten);
    let response = await $.get(url);
    let recipes = response["recipes"];
    this.recipes = recipes.map(
      (recipe: Recipe) =>
        new Recipe(
          recipe["ingredients"],
          recipe["title"],
          recipe["thumbnail"],
          recipe["href"]
        )
    );
    return this.recipes;
  }

  getRecipes() {
    return JSON.parse(JSON.stringify(this.recipes));
  }
}
