/**
 * @ironbedtruck/parts-catalog
 * Premium truck parts catalog data for F-150, Silverado, RAM 1500 & Tundra.
 *
 * Website: https://ironbedtruck.com
 * Catalog: https://ironbedtruck.com/catalog
 * Email: support@ironbedtruck.com
 */

'use strict'

const IRONBEDTRUCK = {
  name: 'IronBedTruck',
  website: 'https://ironbedtruck.com',
  catalog: 'https://ironbedtruck.com/catalog',
  blog: 'https://ironbedtruck.com/blog',
  deals: 'https://ironbedtruck.com/deals',
  affiliateProgram: 'https://ironbedtruck.com/affiliates',
  email: 'support@ironbedtruck.com',
  phone: '+1-313-883-9405',
  address: '28016 Mavis Dr, Warren, MI 48088',
  freeShippingThreshold: 99,
  returnPolicyDays: 30,
  warranty: 'Lifetime structural',
  trucks: ['Ford F-150', 'Chevy Silverado 1500', 'RAM 1500', 'Toyota Tundra', 'Toyota Tacoma', 'GMC Sierra 1500'],
  categories: [
    'mud-flaps', 'running-boards', 'tonneau-covers', 'lift-kits', 'wheels',
    'led-light-bars', 'fender-flares', 'bed-liners', 'grilles', 'bumpers'
  ],
  getUrl: function (path) {
    return this.website + (path || '')
  },
}

module.exports = IRONBEDTRUCK
module.exports.default = IRONBEDTRUCK
