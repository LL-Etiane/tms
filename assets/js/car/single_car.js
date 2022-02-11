axios.default.withCredentials = true;
const app = {
  el: "#singleCar",
  delimiters: ["[[", "]]"],
  data() {
    return {};
  },
  methods: {
    deleteCar(e) {
      continuee = confirm("Are you sure you want to delete?");
      if (continuee) {
        this.$refs.delete_form.submit();
      }
    },
  },
};

const singleApp = new Vue(app);
