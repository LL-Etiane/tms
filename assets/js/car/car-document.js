axios.default.withCredentials = true;
const app = {
  el: "#car-document-container",
  delimiters: ["[[", "]]"],
  data() {
    return {
      showOtherDocInput: false,
      doc: "",
      allGood: false,
    };
  },
  methods: {
    docCHanged() {
      if (this.doc == "other") {
        this.showOtherDocInput = true;
      }
      if (this.doc != "") {
        this.allGood = true;
      }
    },
  },
};

const carDocs = new Vue(app);
