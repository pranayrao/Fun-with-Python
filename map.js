function map() {


    var word = this.text.match(/\w+/g);

    if (word === null) {
        return;
    }

 
    for (var i = 0; i < word.length; i++) {
		emit(word[i].length, { count : 1 });
    }
}
