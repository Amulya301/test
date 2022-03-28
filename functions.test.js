const concat = require(`./functions`);

test(`name`, () => {
  expect(concat("user", "name")).toBe("username");
});

test(`user`, () => {
  expect(concat(1, 2)).toBe(3);
});
