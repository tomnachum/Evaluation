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

  async fetchRecipes(ingredient: any, dairy: boolean, gluten: boolean) {
    let request = `/recipes?contains=${ingredient}`;
    if (dairy) {
      request += `&dairy=True`;
    }
    if (gluten) {
      request += `&gluten=True`;
    }
    let response = await $.get(request);
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
