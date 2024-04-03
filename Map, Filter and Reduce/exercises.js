// Customer object
let customers = [
  {
    id: 1,
    f_name: "Abby",
    l_name: "Thomas",
    gender: "M",
    married: true,
    age: 32,
    expense: 500,
    purchased: ["Shampoo", "Toys", "Book"],
  },
  {
    id: 2,
    f_name: "Jerry",
    l_name: "Tom",
    gender: "M",
    married: true,
    age: 64,
    expense: 100,
    purchased: ["Stick", "Blade"],
  },
  {
    id: 3,
    f_name: "Dianna",
    l_name: "Cherry",
    gender: "F",
    married: true,
    age: 22,
    expense: 1500,
    purchased: ["Lipstik", "Nail Polish", "Bag", "Book"],
  },
  {
    id: 4,
    f_name: "Dev",
    l_name: "Currian",
    gender: "M",
    married: true,
    age: 82,
    expense: 90,
    purchased: ["Book"],
  },
  {
    id: 5,
    f_name: "Maria",
    l_name: "Gomes",
    gender: "F",
    married: false,
    age: 7,
    expense: 300,
    purchased: ["Toys"],
  },
];

const seniorCustomers = customers.filter((customer) => customer.age > 60);
console.log(seniorCustomers);

const customerWithFullName = customers.map(function (customer) {
  let title = "";
  if (customer.gender === "M") {
    title = "Mr.";
  } else if (customer.gender === "F" && customer.married === true) {
    title = "Mrs.";
  } else {
    title = "Miss";
  }
  customer["full_name"] = `${title} ${customer.f_name} ${customer.l_name}`;
  return customer;
});

// console.log(customerWithFullName);
let count = 0;
const accBookCustomer = customers.reduce((acc, curr) => {
  if (curr.purchased.includes("Book")) {
    acc = acc + curr.age;
    count = count + 1;
  }

  return acc;
}, 0);

const avgAgeBookCustomer = Math.round(accBookCustomer / count);

console.log(avgAgeBookCustomer);

const hasYoungCustomer = customers.some((customer) => customer.age <= 10);

console.log(hasYoungCustomer);

const youngCustomer = customers.filter((customer) => customer.age <= 10);

console.log(youngCustomer);

const hasEveryCustomerAPurchase = customers.every(
  (customer) => customer.purchased.length > 0
);
console.log(hasEveryCustomerAPurchase);

const marriedCustomersExpenses = customers
  .filter((customer) => customer.married)
  .reduce((acc, curr) => acc + curr.expense, 0);

console.log(marriedCustomersExpenses);
