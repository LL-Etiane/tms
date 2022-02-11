axios.default.withCredentials = true;

const app = {
  el: "#register-app",
  delimiters: ["[[", "]]"],
  data() {
    return {
      salary_for: "",
      salary_type_id: "",
      isAdvancement: false,
      salary_for_data: [],
      month: new Date().toLocaleDateString("default", { month: "long" }),
      salary_for_error: "",
      selected_type_error: "",
      selected_type_info: "",
      show_other_form: false,
      continuesubmission: true,
      months: [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "Jully",
        "August",
        "September",
        "October",
        "November",
        "December",
      ],
    };
  },
  methods: {
    checkErrors() {
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.$refs.salaryRegisterForm.submit();
        }
      });
    },

    get_type_data() {
      this.salary_for_error = "";
      if (this.salary_for != "" && this.salary_for != "other") {
        axios
          .get("/salary/api/getusers", {
            params: { salaryfor: this.salary_for },
          })
          .then((data) => {
            this.salary_for_data = data.data;
          })
          .catch((error) => {
            this.salary_for_error =
              "There are no user for the selected type. If this is an error, please contact your site admin";
          });
      } else if (this.salary_for == "other") {
        this.show_other_form = true;
      } else {
        this.salary_for_error = "The salary for must not be empty";
      }
    },
    checkIfAlreadyExist() {
      this.selected_type_error = "";
      this.continuesubmission = true;
      this.selected_type_info = "";
      axios
        .get("/salary/api/checkselected", {
          params: {
            type: this.salary_for,
            type_id: this.salary_type_id,
            month: this.month,
          },
        })
        .then((data) => {
          if (!data.data.continue) {
            this.continuesubmission = false;
            this.selected_type_error =
              "The Selected user has already been paid for the current month";
          }
          if (data.data.continue && data.data.info) {
            this.continuesubmission = false;
            this.selected_type_info = data.data.info;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};

Vue.use(VeeValidate);
const registerApp = new Vue(app);
