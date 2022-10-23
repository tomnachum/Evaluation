class Renderer {
  public render(data: any) {
    this.handlebarsHelper(".players-container", "#players-template", {
      players: data,
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
