export default (to, from, next) => {
  if ("token" in localStorage) {
    next()
  } else {
    next('/signin')
  }
}
