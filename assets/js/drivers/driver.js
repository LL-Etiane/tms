axios.default.withCredentials = true;
const app = {
  el: "#singleDriver",
  delimiters: ["[[", "]]"],
  data() {
    return {};
  },
  methods: {
    deleteDriver(e) {
      continuee = confirm("Are you sure you want to delete?");
      if (continuee) {
        this.$refs.delete_form.submit();
      }
    },
  },
};

const singleApp = new Vue(app);
