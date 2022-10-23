class Renderer {
  public render(recipes: any) {
    console.log(recipes);
    this.handlebarsHelper(".recipes-container", "#recipes-template", {
      recipes,
    });
  }

  private handlebarsHelper(
    containerSelector: string,
    templateSelector: string,
    dataObject: any
  ) {
    $(containerSelector).empty();
    const source = $(templateSelector).html();
    const template = Handlebars.compile(source);
    const newHTML = template(dataObject);
    $(containerSelector).append(newHTML);
  }
}
